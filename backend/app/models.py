from pydantic import BaseModel

class ScamAnalysisRequest(BaseModel):
    text: str
