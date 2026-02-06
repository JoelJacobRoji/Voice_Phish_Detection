# aiml/scam_analyzer.py

import os
from pathlib import Path
import joblib

from aiml.audio_features import extract_audio_features
from aiml.inference import transcribe_audio
from aiml.preprocessing import clean_text
from aiml.keyword_engine import keyword_score

# --------------------------------------------------
# Robust path handling (deployment-safe)
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
ARTIFACTS_DIR = BASE_DIR / "artifacts"

TEXT_MODEL_PATH = ARTIFACTS_DIR / "text_model.pkl"
VECTORIZER_PATH = ARTIFACTS_DIR / "text_vectorizer.pkl"

if not TEXT_MODEL_PATH.exists() or not VECTORIZER_PATH.exists():
    raise FileNotFoundError("Model artifacts not found. Run training first.")

text_model = joblib.load(TEXT_MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

# --------------------------------------------------
# Helper: voice risk scoring
# --------------------------------------------------
def voice_risk_score(audio_feats: dict) -> float:
    pitch = audio_feats.get("pitch", 0.0)
    energy = audio_feats.get("energy", 0.0)
    tempo = audio_feats.get("tempo", 0.0)

    risk = 0.0

    if pitch > 220:
        risk += 0.2
    if tempo > 140:
        risk += 0.25
    if energy > 0.05:
        risk += 0.25

    return min(risk, 1.0)

# --------------------------------------------------
# Main analysis pipeline
# --------------------------------------------------
def analyze_call(audio_path: str) -> dict:
    if not os.path.exists(audio_path):
        raise FileNotFoundError("Audio file not found")

    # 1. Speech → Text
    transcript = transcribe_audio(audio_path).strip()

    if not transcript:
        return {
            "transcript": "",
            "risk_score": 0.0,
            "risk_level": "Unknown",
            "matched_phrases": [],
            "audio_features": {},
        }

    # 2. Audio features
    audio_feats = extract_audio_features(audio_path)
    voice_risk = voice_risk_score(audio_feats)

    cleaned_text = clean_text(transcript)

    if not cleaned_text:
        ml_prob = 0.0
    else:
        X = vectorizer.transform([cleaned_text])
        ml_prob = float(text_model.predict_proba(X)[0][1])


    # 4. Keyword engine (FIXED)
    keyword_data = keyword_score(transcript)

    matched_phrases = keyword_data["keyword_hits"]

    keyword_risk_map = {
        "LOW": 0.1,
        "MEDIUM": 0.5,
        "HIGH": 0.9
    }
    keyword_risk = keyword_risk_map.get(keyword_data["keyword_risk"], 0.0)

    # 5. Risk fusion
    final_risk = (
        (ml_prob * 0.5) +
        (keyword_risk * 0.3) +
        (voice_risk * 0.2)
    )

    # 6. Risk level
    if final_risk >= 0.7:
        level = "High"
    elif final_risk >= 0.4:
        level = "Medium"
    else:
        level = "Low"

    return {
        "transcript": transcript,
        "risk_score": round(final_risk * 100, 2),
        "risk_level": level,
        "matched_phrases": matched_phrases,
        "audio_features": audio_feats,
    }
