# Evaluation

Reference scorer for the BOTNOI ASR Telephony Benchmark.

## Install

```bash
pip install -r requirements.txt
```

## Usage

Each submission file is a JSONL manifest with one record per utterance:

```json
{"audio_filepath": "telephony_test/00001.wav", "text": "สวัสดีค่ะ"}
```

Reference manifests follow the same format. The telephony track's reference audio and transcripts are published as a [Hugging Face dataset](https://huggingface.co/datasets/Botnoi/voicebot-telephony-speech) (columns `audio`, `sentence` — not yet in manifest form), so convert it first with `prepare_hf_manifest.py`:

```bash
python prepare_hf_manifest.py --out-dir botnoi_telephony_test

python compute_cer.py \
    --manifest predictions.jsonl \
    --references botnoi_telephony_test/manifest.jsonl
```

The names-and-addresses track's reference manifest is not part of this release; it is available from the maintainers on request.

## Notes

- Text is Unicode NFC-normalised before scoring to avoid spurious mismatches between decomposed and composed Thai sequences.
- The scorer errors out if any reference utterance is missing from predictions rather than silently dropping rows — this avoids inflated CER numbers from partial submissions.
- For the latency track, report RTFx separately, measured on a single A100 40 GB at batch 32 unless otherwise stated.
