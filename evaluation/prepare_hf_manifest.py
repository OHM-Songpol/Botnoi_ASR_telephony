"""Convert the public BOTNOI telephony test set (Hugging Face) into a local
JSONL manifest compatible with compute_cer.py.

Usage:
    python prepare_hf_manifest.py --out-dir botnoi_telephony_test
"""
import argparse
import json
import os
import unicodedata

from datasets import Audio, load_dataset

DATASET_ID = "Botnoi/voicebot-telephony-speech"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", default="botnoi_telephony_test",
                     help="Directory to write audio files and manifest.jsonl into")
    ap.add_argument("--split", default="test")
    args = ap.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)

    ds = load_dataset(DATASET_ID, split=args.split)
    ds = ds.cast_column("audio", Audio(decode=False))

    manifest_path = os.path.join(args.out_dir, "manifest.jsonl")
    with open(manifest_path, "w", encoding="utf-8") as f:
        for i, row in enumerate(ds):
            audio_filepath = os.path.join(args.out_dir, f"{i:05d}.wav")
            with open(audio_filepath, "wb") as af:
                af.write(row["audio"]["bytes"])
            record = {
                "audio_filepath": audio_filepath,
                "text": unicodedata.normalize("NFC", row["sentence"]),
            }
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(f"wrote {len(ds)} utterances to {manifest_path}")


if __name__ == "__main__":
    main()
