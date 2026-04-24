"""Compute character error rate (CER) for a benchmark submission.

Usage:
    python compute_cer.py --manifest predictions.jsonl --references references.jsonl
"""
import argparse
import json
import sys
import unicodedata

from jiwer import cer


def load_manifest(path):
    records = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            key = rec["audio_filepath"]
            records[key] = unicodedata.normalize("NFC", rec["text"])
    return records


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True, help="JSONL of predictions (audio_filepath, text)")
    ap.add_argument("--references", required=True, help="JSONL of references (audio_filepath, text)")
    args = ap.parse_args()

    preds = load_manifest(args.manifest)
    refs = load_manifest(args.references)

    missing = sorted(set(refs) - set(preds))
    if missing:
        print(f"error: {len(missing)} reference utterances are missing from predictions",
              file=sys.stderr)
        for k in missing[:5]:
            print(f"  - {k}", file=sys.stderr)
        sys.exit(1)

    keys = sorted(refs)
    hypotheses = [preds[k] for k in keys]
    references = [refs[k] for k in keys]

    score = cer(references, hypotheses) * 100
    print(f"utterances: {len(keys)}")
    print(f"CER:        {score:.2f}%")


if __name__ == "__main__":
    main()
