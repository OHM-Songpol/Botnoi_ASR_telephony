# Contributing

Thanks for your interest in the BOTNOI ASR Telephony Benchmark. This document explains how to contribute new baselines, bug fixes, or benchmark-protocol improvements.

## Ways to contribute

1. **Submit a new benchmark result.** Open an issue using the *Benchmark submission* template and attach a prediction file plus a short description of your system. Do not submit models trained on the BOTNOI test splits.
2. **Improve the evaluation harness.** Bug fixes and clearer error messages in [`evaluation/`](evaluation/) are always welcome.
3. **Propose a new track.** If you have a use case (e.g., new language, new vertical) that would benefit from a shared telephony benchmark, open a *Feature request* issue to discuss scope before sending code.
4. **Request dataset access.** Use the *Data access request* issue template — see [`data/README.md`](data/README.md) for the full process.

## Ground rules

- Keep changes focused. One topic per pull request.
- Do not upload audio files to this repository. The test sets are hosted separately; see [`data/README.md`](data/README.md).
- Respect privacy. Any example transcripts or snippets you submit must not contain real personal data.
- By submitting a pull request, you agree that your code contribution is licensed under Apache 2.0.

## Pull request checklist

- [ ] The change has a clear, single purpose.
- [ ] Scripts run against the provided sample manifest (`evaluation/sample/`).
- [ ] New dependencies are added to `evaluation/requirements.txt` with pinned versions.
- [ ] Docs under `docs/` are updated if the protocol or contact info changes.

## Reporting issues

Please use the issue templates under [`.github/ISSUE_TEMPLATE/`](.github/ISSUE_TEMPLATE/). For anything involving sensitive data (e.g., you believe a clip in the dataset contains identifiable personal information), email the maintainers directly rather than opening a public issue.
