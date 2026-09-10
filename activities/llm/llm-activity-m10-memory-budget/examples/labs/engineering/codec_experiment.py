"""Record actual byte round trips and full transport costs against gzip."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import random
import time
from .byte_codec import Adaptive, Neural, encode, decode


def experiment(checkpoint, output):
    generator=random.Random(7)
    cases={"empty":b"", "all-bytes":bytes(range(256)),
           "random-256":bytes(generator.randrange(256) for _ in range(256)),
           "synthetic-text":b"Ada studia python nel laboratorio A.\n"*4}
    rows=[]
    for name,data in cases.items():
        for mode,factory in [("adaptive",Adaptive),("neural",lambda:Neural(checkpoint))]:
            start=time.perf_counter()
            archive=encode(data,factory())
            restored=decode(archive,factory())
            if restored!=data:
                raise AssertionError("lossless roundtrip failed")
            shared=checkpoint.stat().st_size if mode=="neural" else 0
            rows.append({"case":name,"mode":mode,"input_bytes":len(data),
                         "archive_bytes_including_header":len(archive),
                         "shared_checkpoint_bytes":shared,
                         "first_transfer_bytes":len(archive)+shared,
                         "gzip_bytes":len(gzip.compress(data,mtime=0)),
                         "roundtrip_sha256":hashlib.sha256(restored).hexdigest(),
                         "elapsed_seconds":time.perf_counter()-start})
    report={"mode":"measured-cpu","cases":rows,"limits":
            "not a claim of better compression; neural CDF needs same numerical environment; not PollicinoNet integration"}
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(report,indent=2)+"\n")
    return report


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--checkpoint',type=Path,default=Path('output/engineering/tiny-byte-lm.pt'))
    parser.add_argument('--output',type=Path,default=Path('output/engineering/codec-report.json'))
    args=parser.parse_args()
    print(json.dumps(experiment(args.checkpoint,args.output),indent=2))
