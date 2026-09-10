"""A byte-level decoder Transformer built from tensors, not a pretrained model."""
from dataclasses import dataclass
import math
import torch
from torch import nn
from torch.nn import functional as F


@dataclass
class Config:
    vocab: int = 256
    width: int = 48
    heads: int = 4
    layers: int = 2
    context: int = 64


class Attention(nn.Module):
    def __init__(self, config):
        super().__init__()
        if config.width % config.heads:
            raise ValueError("width must be divisible by heads")
        self.heads = config.heads
        self.qkv = nn.Linear(config.width, 3 * config.width)
        self.out = nn.Linear(config.width, config.width)

    def forward(self, x, cache=None, fused=False):
        batch, time, width = x.shape
        q, k, v = self.qkv(x).view(batch, time, 3, self.heads, width // self.heads).unbind(2)
        q, k, v = [t.transpose(1, 2) for t in (q, k, v)]
        past = 0 if cache is None else cache[0].size(-2)
        if cache is not None:
            k, v = torch.cat((cache[0], k), dim=-2), torch.cat((cache[1], v), dim=-2)
        allowed = torch.arange(k.size(-2), device=x.device)[None, :] <= (
            past + torch.arange(time, device=x.device)[:, None])
        if fused:
            y = F.scaled_dot_product_attention(q, k, v, attn_mask=allowed, dropout_p=0.0)
        else:
            scores = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1))
            weights = scores.masked_fill(~allowed, float("-inf")).softmax(-1)
            y = weights @ v
        y = y.transpose(1, 2).contiguous().view(batch, time, width)
        return self.out(y), (k, v)


class Block(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.norm1, self.norm2 = nn.LayerNorm(config.width), nn.LayerNorm(config.width)
        self.attention = Attention(config)
        self.mlp = nn.Sequential(nn.Linear(config.width, 4*config.width), nn.GELU(),
                                 nn.Linear(4*config.width, config.width))

    def forward(self, x, cache=None, fused=False):
        attention, cache = self.attention(self.norm1(x), cache, fused)
        x = x + attention
        return x + self.mlp(self.norm2(x)), cache


class TinyLM(nn.Module):
    def __init__(self, config=None):
        super().__init__()
        self.config = config or Config()
        c = self.config
        self.token = nn.Embedding(c.vocab, c.width)
        self.position = nn.Embedding(c.context, c.width)
        self.blocks = nn.ModuleList([Block(c) for _ in range(c.layers)])
        self.norm = nn.LayerNorm(c.width)
        self.head = nn.Linear(c.width, c.vocab, bias=False)

    def forward(self, ids, cache=None, return_cache=False, fused=False):
        if ids.ndim != 2 or ids.size(1) < 1:
            raise ValueError("expected a nonempty [batch,time] tensor")
        if cache is not None and len(cache) != len(self.blocks):
            raise ValueError("one KV pair per block required")
        past = 0 if cache is None else cache[0][0].size(-2)
        if past + ids.size(1) > self.config.context:
            raise ValueError("context limit exceeded; reset cache explicitly")
        positions = torch.arange(past, past + ids.size(1), device=ids.device)
        x = self.token(ids) + self.position(positions)[None, :, :]
        updated = []
        for i, block in enumerate(self.blocks):
            x, kv = block(x, None if cache is None else cache[i], fused)
            updated.append(kv)
        logits = self.head(self.norm(x))
        return (logits, updated) if return_cache else logits


class LoRAHead(nn.Module):
    """Low-rank update on the output projection; base weights stay frozen."""
    def __init__(self, base, rank=4, alpha=8):
        super().__init__()
        if rank <= 0:
            raise ValueError("rank must be positive")
        self.base, self.scale = base, alpha / rank
        self.A = nn.Parameter(torch.randn(rank, base.in_features) * 0.02)
        self.B = nn.Parameter(torch.zeros(base.out_features, rank))
        for parameter in base.parameters():
            parameter.requires_grad_(False)

    def forward(self, x):
        return self.base(x) + F.linear(F.linear(x, self.A), self.B) * self.scale

    def merged_weight(self):
        return self.base.weight + self.scale * self.B @ self.A


def attach_lora(model, rank=4):
    for parameter in model.parameters():
        parameter.requires_grad_(False)
    model.head = LoRAHead(model.head, rank=rank)
    return model
