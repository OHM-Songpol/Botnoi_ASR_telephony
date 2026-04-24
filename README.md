# BOTNOI ASR Telephony Benchmark

Domain-adaptive ASR benchmark and reference fine-tuning recipes for enterprise contact-center telephony, built on NVIDIA Canary Flash models and the NVIDIA NeMo framework.

This repository accompanies the technical report *"Domain-Adaptive ASR for Telephony AI Agents: Fine-tuning Canary Flash Models for Enterprise Contact Center Applications"* (Boonpramuk & Voravuthikunchai, Botnoi Group, 2026).

## What is here

- **Benchmark definition** — evaluation protocol, test splits, and metrics (CER, RTFx) for Thai telephony ASR, business-critical jargon (names and addresses), and latency.
- **Leaderboard** — public results table and submission instructions under [`benchmarks/`](benchmarks/).
- **Data card** — how the BOTNOI telephony dataset was collected, its scope and limitations, and how to request access. See [`data/README.md`](data/README.md).
- **Evaluation scripts** — reference CER/RTFx scoring compatible with NeMo manifests and Hugging Face datasets, under [`evaluation/`](evaluation/).
- **Contribution site** — a small GitHub Pages site (under [`docs/`](docs/)) where external contributors can read the protocol and reach the maintainers.

## Quick start

```bash
git clone https://github.com/<your-org>/botnoi-asr-benchmark.git
cd botnoi-asr-benchmark
pip install -r evaluation/requirements.txt

python evaluation/compute_cer.py \
    --manifest path/to/your_predictions.jsonl \
    --references data/botnoi_telephony_test.jsonl
```

Each line of the predictions file should be JSON with `audio_filepath`, `text` (prediction), and optionally `duration`.

## Headline results (from the technical report)

| Track                                    | Metric | Best off-the-shelf | BOTNOI Canary 180M Flash |
|------------------------------------------|--------|--------------------|--------------------------|
| Thai — Common Voice 23                   | CER    | 7.25               | **4.66**                 |
| Telephony — BOTNOI telephony test        | CER    | 29.05              | **9.04**                 |
| Names and addresses — BOTNOI jargon test | CER    | 22.99              | **10.29**                |
| Latency — single A100, batch 32          | RTFx   | 56.5               | **601.8**                |

## Citation

If you use this benchmark or the associated models, please cite:

```bibtex
@techreport{boonpramuk2026botnoi,
  title  = {Domain-Adaptive ASR for Telephony AI Agents:
            Fine-tuning Canary Flash Models for Enterprise Contact Center Applications},
  author = {Boonpramuk, Chanameth and Voravuthikunchai, Winn},
  year   = {2026},
  institution = {Botnoi Group}
}
```

See also [`CITATION.cff`](CITATION.cff).

## Contributing

We welcome contributions of new baselines, additional telephony domains, and improvements to the evaluation harness. Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening an issue or a pull request.

## Contact

- **Chanameth Boonpramuk** — chanameth.b@botnoigroup.com
- **Winn Voravuthikunchai** — winnv@botnoigroup.com
- Website: https://<your-org>.github.io/botnoi-asr-benchmark/

## License

- **Code** in this repository is released under the Apache License 2.0 (see [`LICENSE`](LICENSE)).
- **Data** is released under separate terms described in [`data/README.md`](data/README.md); access requires agreement to the data-use terms.
