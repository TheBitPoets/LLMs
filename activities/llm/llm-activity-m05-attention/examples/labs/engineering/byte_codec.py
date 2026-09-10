"""Integer arithmetic coding for arbitrary bytes; optional shared neural CDF.

Archive checksums detect corruption, not adversarial tampering. Neural mode
requires the same checkpoint and numerically identical CDFs on both ends.
"""
import argparse
from bisect import bisect_right
import hashlib
import json
from pathlib import Path
import struct

FULL, HALF, QUARTER = 1 << 32, 1 << 31, 1 << 30


class Adaptive:
    identity = "adaptive-order0-v1"
    def __init__(self):
        self.counts = [1]*256

    def frequencies(self):
        return self.counts

    def update(self, byte):
        self.counts[byte] += 1
        if sum(self.counts) >= 16384:
            self.counts = [(c+1)//2 for c in self.counts]


class Neural:
    def __init__(self, checkpoint):
        import torch
        from .train import load_model
        self.torch = torch
        torch.set_num_threads(1)
        torch.use_deterministic_algorithms(True)
        self.model = load_model(checkpoint)
        self.prefix = []
        self.identity = "tiny-byte-cdf-v1:" + hashlib.sha256(Path(checkpoint).read_bytes()).hexdigest()

    def frequencies(self):
        torch = self.torch
        tokens = ([0] + self.prefix)[-self.model.config.context:]
        with torch.inference_mode():
            p = self.model(torch.tensor([tokens]))[0, -1].double().softmax(-1).tolist()
        # Positive integer frequencies, total exactly 4096, stable byte-index tie break.
        real = [value * (4096-256) for value in p]
        counts = [1+int(value) for value in real]
        remainder = 4096-sum(counts)
        order = sorted(range(256), key=lambda i: (-(real[i]-int(real[i])), i))
        for i in order[:remainder]:
            counts[i] += 1
        return counts

    def update(self, byte):
        self.prefix.append(byte)
        self.prefix = self.prefix[-self.model.config.context:]


def cumulative(predictor):
    frequencies = predictor.frequencies()
    if len(frequencies) != 256 or any(type(x) is not int or x < 1 for x in frequencies):
        raise ValueError("positive integer frequencies for 256 bytes required")
    result = [0]
    for value in frequencies:
        result.append(result[-1]+value)
    if result[-1] >= QUARTER:
        raise ValueError("CDF total too large")
    return result


def encode(data, predictor):
    low, high, pending, bits = 0, FULL-1, 0, []
    def emit(bit):
        nonlocal pending
        bits.append(bit)
        bits.extend([1-bit]*pending)
        pending = 0
    for byte in data:
        cdf = cumulative(predictor)
        width = high-low+1
        high = low + width*cdf[byte+1]//cdf[-1]-1
        low += width*cdf[byte]//cdf[-1]
        while True:
            if high < HALF:
                emit(0)
            elif low >= HALF:
                emit(1)
                low -= HALF
                high -= HALF
            elif low >= QUARTER and high < 3*QUARTER:
                pending += 1
                low -= QUARTER
                high -= QUARTER
            else:
                break
            low *= 2
            high = high*2+1
        predictor.update(byte)
    pending += 1
    emit(0 if low < QUARTER else 1)
    payload = bytearray((len(bits)+7)//8)
    for i, bit in enumerate(bits):
        payload[i//8] |= bit << (7-i%8)
    header = {"version": 1, "length": len(data), "bits": len(bits), "predictor": predictor.identity,
              "data_sha256": hashlib.sha256(data).hexdigest(),
              "payload_sha256": hashlib.sha256(payload).hexdigest()}
    encoded_header = json.dumps(header,sort_keys=True,separators=(",", ":")).encode()
    return b"TBC1" + struct.pack(">I",len(encoded_header)) + encoded_header + payload


def decode(archive, predictor, max_output=1_000_000):
    if archive[:4] != b"TBC1" or len(archive) < 8:
        raise ValueError("invalid archive header")
    header_size = struct.unpack(">I",archive[4:8])[0]
    if not 1 <= header_size <= 4096 or len(archive) < 8+header_size:
        raise ValueError("invalid or truncated header")
    header = json.loads(archive[8:8+header_size])
    if (not isinstance(header, dict) or header.get("version") != 1
            or header.get("predictor") != predictor.identity):
        raise ValueError("archive version or predictor mismatch")
    length, bit_count = header.get("length"), header.get("bits")
    if type(length) is not int or not 0 <= length <= max_output or type(bit_count) is not int or bit_count < 2:
        raise ValueError("invalid output or bit budget")
    payload = archive[8+header_size:]
    if len(payload) != (bit_count+7)//8 or hashlib.sha256(payload).hexdigest() != header.get("payload_sha256"):
        raise ValueError("truncated or corrupt payload")
    cursor = 0
    def read():
        nonlocal cursor
        value = (payload[cursor//8] >> (7-cursor%8)) & 1 if cursor < bit_count else 0
        cursor += 1
        return value
    low, high, value, result = 0, FULL-1, 0, bytearray()
    for _ in range(32):
        value = value*2+read()
    for _ in range(length):
        cdf = cumulative(predictor)
        width = high-low+1
        scaled = ((value-low+1)*cdf[-1]-1)//width
        byte = bisect_right(cdf,scaled)-1
        if not 0 <= byte < 256:
            raise ValueError("decoder state outside CDF")
        high = low+width*cdf[byte+1]//cdf[-1]-1
        low += width*cdf[byte]//cdf[-1]
        while True:
            if high < HALF:
                pass
            elif low >= HALF:
                low -= HALF
                high -= HALF
                value -= HALF
            elif low >= QUARTER and high < 3*QUARTER:
                low -= QUARTER
                high -= QUARTER
                value -= QUARTER
            else:
                break
            low *= 2
            high = high*2+1
            value = value*2+read()
        result.append(byte)
        predictor.update(byte)
    if hashlib.sha256(result).hexdigest() != header.get("data_sha256"):
        raise ValueError("decoded checksum mismatch; possible predictor divergence")
    return bytes(result)


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=["encode", "decode"])
    parser.add_argument("source",type=Path)
    parser.add_argument("destination",type=Path)
    parser.add_argument("--checkpoint",type=Path)
    args=parser.parse_args()
    if args.destination.exists():
        parser.error("destination already exists; choose a new path")
    predictor = Neural(args.checkpoint) if args.checkpoint else Adaptive()
    data = args.source.read_bytes()
    result = encode(data,predictor) if args.operation == "encode" else decode(data,predictor)
    args.destination.write_bytes(result)
    print(json.dumps({"input_bytes":len(data), "output_bytes":len(result),"predictor":predictor.identity}))
