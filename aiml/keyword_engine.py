# aiml/keyword_engine.py

SCAM_KEYWORDS = {
    "otp": 0.25,
    "password": 0.25,
    "verify your account": 0.2,
    "bank account": 0.2,
    "urgent": 0.15,
    "immediately": 0.15,
    "suspended": 0.2,
    "click the link": 0.25,
    "wire transfer": 0.3,
    "gift card": 0.3,
    "lottery": 0.25,
    "won prize": 0.25,
    "refund": 0.15,
    "tax department": 0.3,
    "customs": 0.25,
    "police case": 0.35,
    "arrest": 0.4,
    "legal action": 0.35,
}

def keyword_score(text: str):
    """
    Returns:
        keyword_risk (float): 0–1
        matched_phrases (list[str])
    """
    text = text.lower()

    matched_phrases = []
    risk_score = 0.0

    for phrase, weight in SCAM_KEYWORDS.items():
        if phrase in text:
            matched_phrases.append(phrase)
            risk_score += weight

    # Normalize to 0–1
    keyword_risk = min(risk_score, 1.0)

    return keyword_risk, matched_phrases
