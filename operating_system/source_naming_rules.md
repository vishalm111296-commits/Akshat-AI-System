# Source Naming Rules

All files added to `raw_sources/` must follow this convention.

---

## Format

```
[TYPE]-[YYYY-MM-DD]-[SHORT_SLUG].[ext]
```

## Type Codes

| Code | Source Type |
|---|---|
| `YT` | YouTube video transcript |
| `CP` | Public YouTube community post |
| `PP` | Paid community / membership post |
| `INT` | Interview or podcast transcript |
| `ART` | Article or blog post |
| `OTH` | Other |

## Examples

```
YT-2026-06-19-india-vs-us-allocation.txt
CP-2026-05-30-barbell-update.txt
PP-2026-04-15-portfolio-disclosure-q2.txt
```

## Rules

- Use lowercase slug with hyphens only — no spaces, underscores, or special characters
- Date must be the **publication date** of the original content, not the ingestion date
- If publication date is unknown, use `0000-00-00`
- Extension must be `.txt` for all text content
- Never use the word `summary`, `analysis`, or `generated` in the filename — those belong in `docs/` or `changelog/`, not `raw_sources/`
