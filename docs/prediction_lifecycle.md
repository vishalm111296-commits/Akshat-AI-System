# Prediction Lifecycle (L11)

Every prediction within the Akshat-AI-System follows a strict lifecycle. This ensures that every hypothesis is eventually measured against reality.

## The Lifecycle Workflow

```
[ Open Prediction ]
        |
        | (Prediction lives in predictions/open/)
        v
[ Review Date Reached ]
        |
        | (Time horizon matures)
        v
[ Outcome Evaluation ]
        |
        | (Evaluate using outcome_template.md)
        | (Determine CORRECT, INCORRECT, or PARTIALLY_CORRECT)
        v
[ Closed Prediction ]
        |
        | (File moved to predictions/closed/)
        v
[ Performance Database Update ]
        |
        | (Updates metrics in performance/ L12 layer)
```

## State Definitions

1. **Open**: The event has not yet occurred or the time horizon has not elapsed. Resides in `predictions/open/`.
2. **Closed**: The review date was reached, the outcome was evaluated, and the status was determined. Resides in `predictions/closed/`.
3. **Archived**: The prediction was retired before completion (e.g., test files, obsolete templates, invalid premises). Resides in `predictions/archived/`.
