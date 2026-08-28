# Benchmarks and Leaderboard

This directory tracks submitted results against the BOTNOI ASR Telephony Benchmark.

## Tracks

| Track                     | Test set                              | Primary metric | Secondary |
|---------------------------|---------------------------------------|----------------|-----------|
| Thai — public             | Common Voice 23 (Thai), Fleurs (Thai) | CER            | —         |
| Telephony                 | BOTNOI telephony test (10%)           | CER            | —         |
| Domain jargon             | BOTNOI names & addresses test (10%)   | CER            | —         |
| Latency                   | Common Voice 23 (Thai)                | RTFx           | CER       |

## Submitting a result

1. Open an issue using the *Benchmark submission* template.
2. Attach a prediction file — one JSONL per track, each line `{"audio_filepath": "...", "text": "..."}`.
3. Include a short system description: architecture, training data, and whether any dataset releases overlapping the BOTNOI test splits were used.
4. A maintainer reruns `evaluation/compute_cer.py` against the held-out reference manifest and updates [`leaderboard.md`](leaderboard.md).

Submissions trained on or tuned against the BOTNOI test splits will not be accepted.

## Reproducibility

To be listed on the leaderboard, at minimum one of the following must be true:
- The model and inference code are publicly released.
- A containerized evaluation artifact (e.g., a Docker image) is provided to the maintainers for independent verification.
