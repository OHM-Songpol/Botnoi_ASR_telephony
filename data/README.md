# BOTNOI Telephony Dataset — Data Card

## Overview

The BOTNOI telephony dataset is a Thai-language speech corpus collected specifically for adapting ASR models to production voicebot deployments. It combines two complementary sources:

1. **Real voicebot audio** — utterances captured from Botnoi's production telephone voicebot, segmented by the deployed VAD pipeline, and manually transcribed.
2. **Prompted messaging-app recordings** — clean voice messages recorded by volunteers in response to fixed prompts, then converted to telephony-like audio through mu-law compression and additive environmental noise.

Together, these sources form two evaluation tracks:

| Track                     | Hours | Purpose                                  |
|---------------------------|-------|------------------------------------------|
| General telephony         | 77    | Fine-tune and evaluate on open-domain telephony speech |
| Names and addresses       | 104   | Fine-tune and evaluate on business-critical jargon     |

A 90% / 10% train / test split is used for both tracks. Only the 10% test portion is distributed for benchmarking purposes.

## Collection method

Full details are in Section 3.1 of the technical report. Briefly:
- **VAD-segmented voicebot audio** preserves authentic telephony acoustics (8 kHz narrowband, codec compression, realistic packet noise, spontaneous speaking style).
- **Prompted recordings** allow scalable collection with known transcripts, then are augmented with mu-law conversion and environmental noise to approximate telephony channel conditions.

## Intended use

- **In scope.** Benchmarking Thai telephony ASR systems; research on domain adaptation and telephony robustness; fine-tuning voicebot ASR models for enterprise contact-center use.
- **Out of scope.** Speaker identification, voice cloning, surveillance, or any use that could re-identify individual contributors.

## Known limitations

- Thai only. No Vietnamese or other Southeast Asian languages in this release.
- Recordings reflect the acoustic characteristics of Botnoi's production telephony stack; generalization to other carriers or codecs is not guaranteed.
- The names-and-addresses track over-samples location and proper-noun vocabulary; it is not representative of general conversation.

## Ethics and privacy

- All real-call audio was collected and annotated under Botnoi's production consent flow.
- Any utterance containing identifiable personal information that is not the volunteer's own (e.g., third-party names, phone numbers, account IDs) was removed or redacted before inclusion.
- If you believe a clip in the released test set contains information that should be redacted, please email the maintainers directly rather than opening a public issue.

## Accessing the data

The general telephony track's test split (the benchmark set used for the "Telephony" track above) is publicly available on Hugging Face:

**[Botnoi/voicebot-telephony-speech](https://huggingface.co/datasets/Botnoi/voicebot-telephony-speech)**

Download directly, or load with the `datasets` library:

```python
from datasets import load_dataset

ds = load_dataset("Botnoi/voicebot-telephony-speech")
```

The dataset ships as `audio` (embedded WAV) and `sentence` (transcript) columns — not a `compute_cer.py`-ready manifest. To evaluate against it, convert it first with [`evaluation/prepare_hf_manifest.py`](../evaluation/prepare_hf_manifest.py), which writes the audio out to files and produces a matching `audio_filepath`/`text` JSONL manifest.

The names-and-addresses track test split is not included in this release; contact the maintainers for access.

## License

The dataset is released for non-commercial research use. Commercial licensing is available on request — contact the maintainers listed in the top-level [`README.md`](../README.md).
