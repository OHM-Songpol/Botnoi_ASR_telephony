---
name: Benchmark submission
about: Submit results for the BOTNOI ASR Telephony Benchmark leaderboard
title: "[Submission] <System name>"
labels: submission
---

## System description

- **Name:**
- **Architecture:**
- **Parameters:**
- **Training data (high level):**
- **Any overlap with BOTNOI test splits?** yes / no — if yes, explain

## Tracks

Tick the tracks you are submitting to:

- [ ] Thai — public (Common Voice 23, Fleurs)
- [ ] Telephony
- [ ] Names and addresses
- [ ] Latency

## Files

Attach a JSONL prediction manifest per track. One line per utterance:

```json
{"audio_filepath": "telephony_test/00001.wav", "text": "..."}
```

## Reproducibility

- Model release (URL or "container available on request"):
- Inference code:

## Contact

- Email (for follow-up if the file cannot be reproduced):
