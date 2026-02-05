from aiml.inference import ScamInferencePipeline

class AIMLService:
    def __init__(self):
        self.pipeline = ScamInferencePipeline()

    def analyze_text(self, text: str):
        prob = self.pipeline.predict_proba(text)
        return {
            "ml_risk_score": float(prob)
        }
