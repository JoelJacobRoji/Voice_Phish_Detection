from pathlib import Path

# Base directory: aiml/
BASE_DIR = Path(__file__).resolve().parent

# Model artifacts
MODEL_PATH = BASE_DIR / "artifacts" / "scam_model.pkl"
VECTORIZER_PATH = BASE_DIR / "artifacts" / "vectorizer.pkl"
