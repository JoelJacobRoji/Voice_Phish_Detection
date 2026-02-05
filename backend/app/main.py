from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from aiml.scam_analyzer import analyze_call
import os
import shutil
import uuid

app = FastAPI(
    title="Audio Call Scam Analyzer",
    description="API to analyze audio calls for scam risk using speech, text, and voice features",
    version="1.0.0"
)

# --------------------------------------------------
# CORS (frontend + cloud deployment safe)
# --------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------
# Root & health routes
# --------------------------------------------------
@app.get("/")
def root():
    return {
        "message": "Audio Call Scam Analyzer API is running",
        "endpoints": {
            "analyze_audio": "POST /analyze-audio",
            "health": "GET /health"
        }
    }

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "audio-scam-analyzer"
    }

# --------------------------------------------------
# Audio analysis endpoint
# --------------------------------------------------
@app.post("/analyze-audio")
async def analyze_audio(file: UploadFile = File(...)):

    # ---------- VALIDATION ----------
    allowed_extensions = (".wav", ".mp3", ".m4a", ".ogg")
    filename = file.filename.lower()

    if not (
        (file.content_type and file.content_type.startswith("audio/"))
        or filename.endswith(allowed_extensions)
    ):
        raise HTTPException(
            status_code=400,
            detail="Uploaded file must be an audio file"
        )

    # ---------- TEMP FILE ----------
    os.makedirs("temp", exist_ok=True)
    temp_filename = f"{uuid.uuid4()}_{file.filename}"
    temp_path = os.path.join("temp", temp_filename)

    try:
        # Save uploaded file
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Run analysis
        result = analyze_call(temp_path)

        if not result or "risk_score" not in result:
            raise HTTPException(
                status_code=500,
                detail="Analysis failed or returned invalid result"
            )

        return result

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal error: {str(e)}"
        )

    finally:
        # Cleanup
        try:
            if os.path.exists(temp_path):
                os.remove(temp_path)
        except Exception:
            pass
