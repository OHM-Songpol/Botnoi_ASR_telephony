# Leaderboard

Last updated: 2026-04-24

## Telephony track — CER (%)

| Rank | System                               | CER   | Notes                         |
|------|--------------------------------------|-------|-------------------------------|
| 1    | BOTNOI Canary 180M Flash (telephony) | 9.04  | This work                     |
| 2    | BOTNOI Canary 180M Flash (lang only) | 23.31 | This work — telephony-agnostic |
| 3    | Whisper-large-v3                     | 29.05 | Off-the-shelf                 |

## Names and addresses track — CER (%)

| Rank | System                                           | CER   | Notes                     |
|------|--------------------------------------------------|-------|---------------------------|
| 1    | BOTNOI Canary 180M Flash (with names/addresses)  | 10.29 | This work                 |
| 2    | BOTNOI Canary 180M Flash (telephony only)        | 16.98 | This work                 |
| 3    | Whisper-large-v3                                 | 22.99 | Off-the-shelf             |

## Latency — CER vs. RTFx (single A100, batch 32)

| System                   | CER  | RTFx    |
|--------------------------|------|---------|
| Canary 180M Flash        | 2.88 | 601.80  |
| Canary 1B Flash          | 2.78 | 531.43  |
| Distil-whisper-large-v3  | 5.12 | 75.38   |
| Whisper-large-v3         | 7.75 | 56.53   |
