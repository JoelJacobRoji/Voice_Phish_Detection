import pandas as pd

INPUT_PATH = "aiml/data/SMSSpamCollection"
OUTPUT_PATH = "aiml/data/sms_spam.csv"

data = []

with open(INPUT_PATH, "r", encoding="utf-8") as f:
    for line in f:
        label, text = line.strip().split("\t", 1)
        data.append({
            "text": text,
            "label": 1 if label == "spam" else 0
        })

df = pd.DataFrame(data)
df.to_csv(OUTPUT_PATH, index=False)

print("✅ Dataset converted and saved as sms_spam.csv")
