---
layout: default
title: Home
---

# BOTNOI ASR Telephony Benchmark

A public benchmark and reference fine-tuning recipes for **Thai telephony ASR** in enterprise contact-center settings, built on NVIDIA Canary Flash models and the NVIDIA NeMo framework.

This site is the contributor-facing landing page for the [GitHub repository](https://github.com/<your-org>/botnoi-asr-benchmark). For the full technical report, see *"Domain-Adaptive ASR for Telephony AI Agents: Fine-tuning Canary Flash Models for Enterprise Contact Center Applications"* (Boonpramuk & Voravuthikunchai, Botnoi Group, 2026).

## Why this benchmark

Most public ASR benchmarks are recorded at 16 kHz in quiet conditions. Production voicebots see the opposite: 8 kHz narrowband, codec compression, spontaneous speech, and heavy background noise. This benchmark is the first public, Thai-focused evaluation designed specifically for those conditions, with dedicated tracks for:

- **General telephony** — open-domain Thai telephony speech.
- **Names and addresses** — business-critical jargon that drives real downstream errors.
- **Latency** — RTFx at realistic batch sizes on a single A100.

## Headline results

| Track                     | Best off-the-shelf | BOTNOI Canary 180M Flash |
|---------------------------|--------------------|--------------------------|
| Telephony (CER)           | 29.05              | **9.04**                 |
| Names & addresses (CER)   | 22.99              | **10.29**                |
| Latency (RTFx @ A100, bs 32) | 56.5            | **601.8**                |

Full leaderboard: [`benchmarks/leaderboard.md`](../benchmarks/leaderboard.md).

## Get involved

- [Submit a result](submit.html)
- [Request dataset access](access.html)
- [Contact the team](contact.html)

## Citation

```bibtex
@techreport{boonpramuk2026botnoi,
  title  = {Domain-Adaptive ASR for Telephony AI Agents:
            Fine-tuning Canary Flash Models for Enterprise Contact Center Applications},
  author = {Boonpramuk, Chanameth and Voravuthikunchai, Winn},
  year   = {2026},
  institution = {Botnoi Group}
}
```
