import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

DATA_PATH = "aiml/data/sms_spam.csv"
MODEL_PATH = "aiml/artifacts/text_model.pkl"
VECT_PATH = "aiml/artifacts/text_vectorizer.pkl"

df = pd.read_csv(DATA_PATH)

X = df["text"]
y = df["label"]

vectorizer = TfidfVectorizer(
    stop_words="english",
    ngram_range=(1, 2),
    max_features=8000
)

X_vec = vectorizer.fit_transform(X)

model = LogisticRegression(max_iter=1000)
model.fit(X_vec, y)

joblib.dump(model, MODEL_PATH)
joblib.dump(vectorizer, VECT_PATH)

print("✅ Text scam model trained & saved")
