# Scoring Framework (L12)

This document defines the metrics used to evaluate the accuracy and calibration of the predictions stored in the `predictions/closed/` directory.

*(Note: This is a conceptual knowledge framework. The Akshat-AI-System does not execute Python scripts or use automated databases to calculate these metrics. They are calculated and reported based on the knowledge records.)*

## Core Metrics

### 1. Overall Accuracy
**Definition**: The baseline win rate of all closed predictions.
**Formula**:
`Overall Accuracy = (Correct Predictions + (Partially Correct * 0.5)) / Total Closed Predictions`
**Example**:
Out of 100 predictions, 60 are CORRECT, 10 are PARTIALLY_CORRECT, and 30 are INCORRECT.
`Overall Accuracy = (60 + 5) / 100 = 65%`

### 2. Sector Accuracy
**Definition**: Win rate segmented by market sector (e.g., Tech, Real Estate, Healthcare).
**Formula**:
`Sector Accuracy = (Correct in Sector + (Partially Correct in Sector * 0.5)) / Total Predictions in Sector`

### 3. Theme Accuracy
**Definition**: Win rate segmented by macro theme (e.g., "India Consumption", "AI Infrastructure").
**Formula**:
`Theme Accuracy = (Correct in Theme + (Partially Correct in Theme * 0.5)) / Total Predictions in Theme`

### 4. Confidence Calibration
**Definition**: Measures how accurately the "Confidence" percentage assigned to a prediction aligns with the actual success rate.
**Concept**: If 10 predictions are made with "80% Confidence", approximately 8 of them should be correct.
**Example**:
- Predictions marked 80% Confidence: Actual success rate = 78% (Excellent calibration)
- Predictions marked 90% Confidence: Actual success rate = 50% (Poor calibration, overconfident)

### 5. Win Rate
**Definition**: A strict binary metric that does not grant partial credit.
**Formula**:
`Win Rate = Correct Predictions / Total Closed Predictions`

### 6. Error Analysis
**Definition**: A qualitative review of INCORRECT predictions to identify systemic flaws in reasoning.
**Focus Areas**:
- Was the timing wrong, but the thesis right?
- Were the supporting beliefs flawed?
- Did an unforeseen macro event invalidate the prediction?
