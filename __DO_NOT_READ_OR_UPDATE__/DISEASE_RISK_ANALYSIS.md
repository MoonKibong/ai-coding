# Feature: Disease Risk Analysis

**Status**: 🚧 In Progress
**Route**: `/analysis`
**API**: `POST /api/v1/predict`

## Overview
A diagnostic tool that accepts patient vitals and returns a calculated disease risk score with visual explanations.

## User Stories
- As a **Doctor**, I want to input patient vitals (Age, BMI, BP) so that I can see their immediate risk profile.
- As a **User**, I want to see a visual comparison against "Healthy" baselines to understand which factors contribute most to the risk.

## Data Contract (The Contract)

**Input (PatientVitals)**
```json
{
  "age": 45,             // int, 1-120
  "bmi": 24.5,           // float, 10-60
  "systolic_bp": 120,    // int, 70-200
  "is_smoker": false     // boolean
}

**Output (RiskAssessment)**
```json
{
  "risk_score": 35.5,    // float, 0-100
  "risk_level": "LOW",   // enum: LOW, MODERATE, HIGH
  "factors": {           // contributors to the score
    "age_factor": 10,
    "bmi_factor": 5
  }
}
```

## UI/UX Design

**Input Section**:

- Use v-slider for Age and BMI (visual feedback).

- Use v-switch for boolean flags (Smoker).

**Result Section**:

- Gauge Chart: Show overall risk_score (Green < 30, Yellow < 60, Red > 60).

- Radar Chart: Compare patient metrics vs. hardcoded "Healthy Baseline".

- Dataset 1: Patient [Age/100, BMI/50, BP/200]

- Dataset 2: Healthy [0.3, 0.4, 0.6]

## Logic (Mock AI Engine)

Since the real AI is unavailable, implement this Heuristic Logic:

1. Base score = 0

2. If age > 50 → +20 points

3. If bmi > 30 → +30 points

4. If smoker → +25 points

5. Latency: Must simulate 500ms delay to mimic model inference.