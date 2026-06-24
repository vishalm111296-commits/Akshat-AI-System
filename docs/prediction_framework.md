# Prediction Framework (L11)

This document outlines how predictions are created, reviewed, and archived within the Akshat-AI-System. Predictions form the core of the system's shift from pure knowledge storage into a continuous forecasting and validation system.

## 1. Creating Predictions

Predictions are created when new evidence suggests a future event or trend.
All active predictions are stored in `predictions/open/`.

When creating a new prediction:
1. Copy `predictions/templates/prediction_template.md`.
2. Fill out all fields, including the specific prediction statement, confidence percentage, time horizon, and specific expected outcomes.
3. Link the prediction to supporting beliefs and verified raw sources in the knowledge base.
4. Save the file with the format `YYYY-MM-DD_Short_Description.md`.

## 2. Reviewing Predictions

Each prediction must have a "Review Date". When that date is reached, the prediction is evaluated.

1. Evaluate the actual outcome against the "Expected Outcome".
2. Use `predictions/templates/outcome_template.md` to document the result.
3. Attach the outcome template to the original prediction record.
4. Update the prediction's "Status" field to one of:
   - `CORRECT`
   - `INCORRECT`
   - `PARTIALLY_CORRECT`

## 3. Archiving Predictions

Once a prediction has been reviewed and its outcome documented, it is no longer "open".

1. Move the completed prediction file (which now contains the outcome data) from `predictions/open/` to `predictions/closed/`.
2. The `closed/` directory serves as the immutable long-term statistical database for calculating accuracy metrics.
3. If a prediction is canceled or deprecated before review (e.g., an asset is delisted or the underlying thesis becomes instantly obsolete), it should be moved to `predictions/archived/`. The `archived/` folder is reserved for obsolete templates, deprecated examples, and retired records that should not count towards statistical scoring.
