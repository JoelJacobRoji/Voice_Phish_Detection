## AIML Module – Scam Detection

This module provides:
- Text preprocessing
- Keyword-based risk scoring
- ML-based scam probability (Logistic Regression + TF-IDF)

### Output (used by backend)
- keyword_score (0–100)
- ml_probability (0–1)
- detected_keywords

### IMPORTANT
This module does NOT:
- Decide Scam/Safe
- Generate alerts
- Compute final risk

Those are backend responsibilities.
