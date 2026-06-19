# Environment Setup

## Prerequisites

- Python 3.11+
- Git
- GitHub account with Actions enabled

## One-Time Setup

```bash
bash scripts/bootstrap.sh
```

This installs all dependencies and validates the knowledge file structure.

## Manual Setup

```bash
pip install -r requirements.txt
```

## Dependencies

| Package | Purpose |
|---|---|
| `youtube-transcript-api` | Fetch YouTube video transcripts (free, no API key) |
| `feedparser` | Parse RSS feeds for community posts |
| `pyyaml` | Read config.yaml |
| `pytest` | Test framework |
| `python-dateutil` | Date parsing for source metadata |

## GitHub Actions Free Tier

- 2,000 minutes/month on free tier
- Estimated usage: ~60 min/month (weekly fetches + updates)
- Well within free limits

## Branch Protection

Set the following branch protection rule on `main`:
- Require pull request for any commit touching `knowledge/01_Akshat_Master_System.md`
- The automation bot commits are blocked from this file by code logic in `constants.py`

## Folder Permissions Summary

| Folder | Automation Write | Human Write |
|---|---|---|
| `knowledge/01_*` | ❌ NEVER | ✅ Manual only |
| `knowledge/02_*` | ✅ Auto | ✅ Manual |
| `knowledge/03_*` | ✅ Auto | ✅ Manual |
| `knowledge/04_*` | ✅ Auto | ✅ Manual |
| `raw_sources/` | ✅ Auto (append only) | ✅ Manual |
| `changelog/` | ✅ Auto | ✅ Manual |
