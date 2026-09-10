import copy
from itertools import product
from pathlib import Path
import random
import tempfile
import unittest
import torch
from labs.engineering.tiny_lm import TinyLM, Config, attach_lora
from labs.engineering.inference import reference_attention, tiled_attention
from labs.engineering.train import train_steps, loss_on
from labs.engineering.byte_codec import Adaptive, Neural, encode, decode


class NeuralChecks(unittest.TestCase):
    def setUp(self):
        torch.set_num_threads(1)
        torch.manual_seed(7)
        self.model = TinyLM(Config(width=16,heads=2,layers=1,context=16))

    def test_causality_and_cached_decode(self):
        ids = torch.randint(0,256,(1,12))
        changed = ids.clone()
        changed[:,7:] = (changed[:,7:]+1)%256
        with torch.no_grad():
            full = self.model(ids)
            torch.testing.assert_close(full[:,:7],self.model(changed)[:,:7])
            cache, chunks = None, []
            for i in range(12):
                logits, cache = self.model(ids[:,i:i+1],cache,True)
                chunks.append(logits)
            torch.testing.assert_close(torch.cat(chunks,1),full,atol=1e-6,rtol=1e-5)
        with self.assertRaises(ValueError):
            self.model(torch.zeros(1,17,dtype=torch.long))

    def test_tiled_and_library_attention(self):
        q,k,v=[torch.randn(2,2,19,8) for _ in range(3)]
        reference=reference_attention(q,k,v)
        torch.testing.assert_close(tiled_attention(q,k,v,7),reference,atol=1e-6,rtol=1e-5)
        torch.testing.assert_close(torch.nn.functional.scaled_dot_product_attention(q,k,v,is_causal=True),reference)

    def test_loss_decreases_on_learnable_sequence(self):
        data=torch.tensor(list(b'abcd '*60))
        initial=loss_on(self.model,data)
        train_steps(self.model,data,data,steps=30,lr=0.02)
        self.assertLess(loss_on(self.model,data),initial*0.6)

    def test_lora_initial_identity_gradients_and_merge(self):
        ids=torch.randint(0,256,(1,8))
        before=self.model(ids).detach()
        adapted=attach_lora(copy.deepcopy(self.model),rank=2)
        torch.testing.assert_close(adapted(ids),before)
        torch.nn.functional.cross_entropy(adapted(ids).flatten(0,1),ids.flatten()).backward()
        self.assertIsNotNone(adapted.head.B.grad)
        self.assertGreater(adapted.head.B.grad.abs().sum().item(),0)
        self.assertTrue(all(p.grad is None for n,p in adapted.named_parameters() if n not in {'head.A','head.B'}))
        with torch.no_grad():
            adapted.head.B.add_(0.1)
        x=torch.randn(3,16)
        torch.testing.assert_close(adapted.head(x),torch.nn.functional.linear(x,adapted.head.merged_weight()))


class CodecChecks(unittest.TestCase):
    def test_arbitrary_bytes_and_empty(self):
        randomizer=random.Random(7)
        cases=[b'',bytes(range(256)),bytes(1024),bytes(randomizer.randrange(256) for _ in range(2048)),'Caffè €'.encode()]
        for data in cases:
            with self.subTest(length=len(data)):
                self.assertEqual(decode(encode(data,Adaptive()),Adaptive()),data)

    def test_exhaustive_short_byte_strings(self):
        for length in range(5):
            for values in product([0,127,255],repeat=length):
                data=bytes(values)
                self.assertEqual(decode(encode(data,Adaptive()),Adaptive()),data)

    def test_corruption_truncation_and_budget(self):
        archive=encode(b'hello'*20,Adaptive())
        for corrupt in [archive[:-1],archive[:10],archive[:-1]+bytes([archive[-1]^1])]:
            with self.assertRaises(ValueError):
                decode(corrupt,Adaptive())
        with self.assertRaises(ValueError):
            decode(archive,Adaptive(),max_output=10)

    def test_neural_roundtrip_and_checkpoint_binding(self):
        from dataclasses import asdict
        torch.set_num_threads(1)
        torch.manual_seed(7)
        model=TinyLM(Config(width=8,heads=2,layers=1,context=8))
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'model.pt'
            torch.save({'config':asdict(model.config),'state_dict':model.state_dict()},path)
            data=b'\x00\xffhello'
            archive=encode(data,Neural(path))
            self.assertEqual(decode(archive,Neural(path)),data)
            with self.assertRaises(ValueError):
                decode(archive,Adaptive())


if __name__=='__main__':
    unittest.main()
