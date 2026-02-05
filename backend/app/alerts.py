def alert_message(label: str, risk_score: float) -> str:
    """
    Returns a human-readable alert message based on risk level.
    """

    if label == "SAFE":
        return "✅ No scam detected. Conversation appears safe."

    if label == "SUSPICIOUS":
        return "⚠️ Suspicious content detected. Proceed with caution."

    if label == "SCAM":
        return "🚨 Scam detected! Do NOT share personal or financial details."

    return "ℹ️ Analysis complete."
