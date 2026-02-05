# aiml/preprocessing.py
import re

def clean_text(text: str | None) -> str:
    """
    Safe text cleaner for ML inference.
    NEVER throws.
    """
    if not text or not isinstance(text, str):
        return ""

    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()

    return text
