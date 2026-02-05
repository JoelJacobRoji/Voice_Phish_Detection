from backend.app.config import (
    KEYWORD_WEIGHT,
    ML_WEIGHT,
    SAFE_THRESHOLD,
    SUSPICIOUS_THRESHOLD,
)

def compute_risk(keyword_score: float, ml_score: float) -> dict:
    """
    Combines keyword + ML scores into a final risk score.
    """

    final_score = (
        KEYWORD_WEIGHT * keyword_score +
        ML_WEIGHT * ml_score
    )

    if final_score < SAFE_THRESHOLD:
        label = "SAFE"
    elif final_score < SUSPICIOUS_THRESHOLD:
        label = "SUSPICIOUS"
    else:
        label = "SCAM"

    return {
        "risk_score": round(final_score, 2),
        "label": label
    }
