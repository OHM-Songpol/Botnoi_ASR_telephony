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

Reference manifests follow the same format. The telephony track's reference manifest is distributed with the [public Hugging Face test set](https://huggingface.co/datasets/Botnoi/voicebot-telephony-speech); the names-and-addresses track's reference manifest is available from the maintainers on request.

```bash
python compute_cer.py \
    --manifest predictions.jsonl \
    --references botnoi_telephony_test.jsonl
```

## Notes

- Text is Unicode NFC-normalised before scoring to avoid spurious mismatches between decomposed and composed Thai sequences.
- The scorer errors out if any reference utterance is missing from predictions rather than silently dropping rows — this avoids inflated CER numbers from partial submissions.
- For the latency track, report RTFx separately, measured on a single A100 40 GB at batch 32 unless otherwise stated.
