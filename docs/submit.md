---
layout: default
title: Submit
---

# Submitting a result

1. Read the [evaluation protocol](../evaluation/README.md).
2. Run your model on the track(s) you want to submit to and produce a JSONL manifest per track:

   ```json
   {"audio_filepath": "telephony_test/00001.wav", "text": "..."}
   ```
3. Open a [Benchmark submission issue](https://github.com/OHM-Songpol/Botnoi_ASR_telephony/issues/new?template=benchmark_submission.md) and attach the manifest(s).
4. A maintainer reruns `evaluation/compute_cer.py` against the held-out reference and updates the leaderboard.

## Rules

- **Do not** train or tune on any of the BOTNOI test splits.
- **Do** declare the training data you used — transparency helps downstream users interpret the number.
- To appear on the leaderboard, at least one of the following must be true:
  - The model and inference code are publicly released, or
  - A containerized evaluation artifact is provided for independent verification.

## Latency track

RTFx must be measured on a single NVIDIA A100 40 GB at batch size 32 unless otherwise stated. Include the GPU driver version and the batch configuration in your submission.
