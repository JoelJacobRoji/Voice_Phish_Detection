from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
import tempfile
import shutil

# -----------------------------
# Safe AIML import (Render-safe)
# -----------------------------
try:
    from aiml.scam_analyzer import analyze_call
    MODEL_READY = True
except Exception as e:
    print("⚠️ AIML not ready:", e)
    analyze_call = None
    MODEL_READY = False

# -----------------------------
# FastAPI App
# -----------------------------
app = FastAPI(title="Audio Scam Analyzer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # dev-safe
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Health Check
# -----------------------------
@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "audio-scam-analyzer",
        "model_ready": MODEL_READY
    }

# -----------------------------
# Audio Analysis API
# -----------------------------
@app.post("/analyze-audio")
async def analyze_audio(file: UploadFile = File(...)):

    if not MODEL_READY:
        raise HTTPException(
            status_code=503,
            detail="Model not ready on server"
        )

    # Save temp audio
    suffix = os.path.splitext(file.filename)[1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        shutil.copyfileobj(file.file, tmp)
        temp_path = tmp.name

    try:
        result = analyze_call(temp_path)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)
