# aiml/inference.py

from pathlib import Path
import whisper

# --------------------------------------------------
# Lazy-loaded Whisper model (safe for FastAPI)
# --------------------------------------------------
_whisper_model = None

def _load_model():
    global _whisper_model
    if _whisper_model is None:
        _whisper_model = whisper.load_model("base")
    return _whisper_model


# --------------------------------------------------
# Public API: Speech → Text
# --------------------------------------------------
def transcribe_audio(audio_path: str) -> str:
    audio_path = Path(audio_path)

    if not audio_path.exists():
        raise FileNotFoundError("Audio file not found")

    model = _load_model()

    result = model.transcribe(
        str(audio_path),
        language="en",
        fp16=False  # CPU-safe, deployment-safe
    )

    text = result.get("text", "")
    return text.strip()
