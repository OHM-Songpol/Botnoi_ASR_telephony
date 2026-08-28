---
layout: default
title: Home
---

# BOTNOI ASR Telephony Benchmark

A public benchmark and reference fine-tuning recipes for **Thai telephony ASR** in enterprise contact-center settings, built on NVIDIA Canary Flash models and the NVIDIA NeMo framework.

This site is the contributor-facing landing page for the [GitHub repository](https://github.com/OHM-Songpol/Botnoi_ASR_telephony). For the full paper, see *"Domain-Adaptive ASR for Telephony AI Agents: Fine-tuning Canary Flash Models for Enterprise Contact Center Applications"* (Boonpramuk, Voravuthikunchai & Bunyang, Botnoi Group, 2026), available on [arXiv](http://arxiv.org/abs/2608.24916).

The telephony benchmark data is publicly available on Hugging Face: [Botnoi/voicebot-telephony-speech](https://huggingface.co/datasets/Botnoi/voicebot-telephony-speech).

## Why this benchmark

Most public ASR benchmarks are recorded at 16 kHz in quiet conditions. Production voicebots see the opposite: 8 kHz narrowband, codec compression, spontaneous speech, and heavy background noise. This benchmark is the first public, Thai-focused evaluation designed specifically for those conditions, with dedicated tracks for:

- **General telephony** — open-domain Thai telephony speech.
- **Names and addresses** — business-critical jargon that drives real downstream errors.
- **Latency** — RTFx at realistic batch sizes on a single A100.

## Headline results

| Track                        | Whisper-large-v3 | BOTNOI Canary 180M Flash |
|-------------------------------|-------------------|---------------------------|
| Thai — Common Voice 23 (CER)  | 7.25              | **4.66**                  |
| Telephony (CER)               | 48.44             | **9.04**                  |
| Names & addresses (CER)       | 22.99             | **3.78**                  |
| Latency (RTFx @ A100, bs 32)  | 56.5              | **601.8**                 |

Whisper-large-v3 is shown as a consistent reference point; the paper also compares against ElevenLabs Scribe v2 and Google Chirp 3, which are stronger on some tracks. Full leaderboard: [`benchmarks/leaderboard.md`](../benchmarks/leaderboard.md).

## Get involved

- [Submit a result](submit.html)
- [Access the dataset](access.html)
- [Contact the team](contact.html)

## Citation

```bibtex
@techreport{boonpramuk2026botnoi,
  title  = {Domain-Adaptive ASR for Telephony AI Agents:
            Fine-tuning Canary Flash Models for Enterprise Contact Center Applications},
  author = {Boonpramuk, Chanameth and Voravuthikunchai, Winn and Bunyang, Songpol},
  year   = {2026},
  institution = {Botnoi Group},
  eprint = {2608.24916},
  archivePrefix = {arXiv},
  url    = {http://arxiv.org/abs/2608.24916}
}
```
