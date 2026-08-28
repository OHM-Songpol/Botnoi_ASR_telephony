# Leaderboard

Last updated: 2026-08-28 — figures taken from the paper (arXiv:2608.24916).

## Thai track — CER (%)

| Rank | System                | Common Voice 23 | Fleurs | Notes                  |
|------|------------------------|------------------|--------|-------------------------|
| 1    | ElevenLabs Scribe v2   | 1.92             | 6.23   | Commercial, off-the-shelf |
| 2    | Google Chirp 3         | 3.46             | 10.29  | Commercial, off-the-shelf |
| 3    | BOTNOI Canary 180M Flash | 4.66           | 9.77   | This work               |
| 4    | Whisper-large-v3       | 7.25             | 8.85   | Open-source, off-the-shelf |

BOTNOI Canary outperforms Whisper-large-v3 on both public Thai sets; ElevenLabs Scribe v2 and Google Chirp 3 remain stronger on this clean read-speech evaluation. BOTNOI Canary's advantage shows up under telephony conditions (see below).

## Telephony track — CER (%)

| Rank | System                                | CER   | Notes                          |
|------|----------------------------------------|-------|---------------------------------|
| 1    | BOTNOI Canary 180M Flash (telephony)  | 9.04  | This work                       |
| 2    | Google Chirp 3                         | 13.42 | Commercial, off-the-shelf       |
| 3    | ElevenLabs Scribe v2                   | 19.68 | Commercial, off-the-shelf       |
| 4    | BOTNOI Canary 180M Flash (non-telephony) | 23.31 | This work — telephony-agnostic baseline |
| 5    | Whisper-large-v3                       | 48.44 | Open-source, off-the-shelf      |

## Names and addresses track — CER (%)

| Rank | System                                             | CER   | Notes                     |
|------|------------------------------------------------------|-------|----------------------------|
| 1    | BOTNOI Canary 180M Flash (telephony + names/addresses) | 3.78 | This work                 |
| 2    | Google Chirp 3                                       | 9.86  | Commercial, off-the-shelf |
| 3    | ElevenLabs Scribe v2                                 | 14.76 | Commercial, off-the-shelf |
| 4    | BOTNOI Canary 180M Flash (telephony only)            | 16.98 | This work                 |
| 5    | Whisper-large-v3                                     | 22.99 | Open-source, off-the-shelf |

Note: the names-and-addresses adaptation trades off slightly against general telephony accuracy — the same checkpoint scores 10.89% CER on the telephony track (vs. 9.04% for the telephony-only checkpoint).

## Latency — CER vs. RTFx (single A100, batch 32, Common Voice 23 Thai)

Measured on the final telephony-adapted checkpoints (so CER here differs from the Thai-track table above, which uses language-adaptation-only checkpoints).

| System                   | CER  | RTFx    |
|--------------------------|------|---------|
| BOTNOI Canary 180M Flash | 2.87 | 601.8   |
| BOTNOI Canary 1B Flash   | 2.73 | 531.4   |
| BOTNOI Distil-whisper-large-v3 | 3.94 | 75.4 |
| Whisper-large-v3         | 7.25 | 56.5    |

Canary 180M Flash is used in production: it nearly matches Canary 1B Flash's accuracy at roughly 6x lower latency and a smaller memory footprint.
