---
layout: default
title: Data access
---

# Data access

The BOTNOI telephony track's benchmark test set is publicly available on Hugging Face:

**[Botnoi/voicebot-telephony-speech](https://huggingface.co/datasets/Botnoi/voicebot-telephony-speech)**

```python
from datasets import load_dataset

ds = load_dataset("Botnoi/voicebot-telephony-speech")
```

To score submissions against it with `evaluation/compute_cer.py`, first convert it to a manifest with `evaluation/prepare_hf_manifest.py` — see the [evaluation README](https://github.com/OHM-Songpol/Botnoi_ASR_telephony/blob/main/evaluation/README.md).

The names-and-addresses track test set is not included in this release — contact the maintainers if you need it.

## Commercial use

Commercial licensing is available on request. Email the maintainers listed on the [contact page](contact.html).

## Full data card

See [`data/README.md`](../data/README.md) in the repository for collection methodology, scope, limitations, and ethics notes.
