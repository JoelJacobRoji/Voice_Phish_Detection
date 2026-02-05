from pathlib import Path
import pandas as pd
import joblib
from aiml.model import ScamClassifier

BASE_DIR = Path(__file__).parent
DATA_PATH = BASE_DIR / "data" / "scam_data.csv"
ARTIFACTS_DIR = BASE_DIR / "artifacts"
MODEL_PATH = ARTIFACTS_DIR / "scam_model.pkl"

def train():
    ARTIFACTS_DIR.mkdir(exist_ok=True)

    df = pd.read_csv(DATA_PATH)
    print("CSV columns:", df.columns.tolist())

    model = ScamClassifier()
    model.fit(df["text"].tolist(), df["label"].tolist())

    joblib.dump(model, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")

if __name__ == "__main__":
    train()
