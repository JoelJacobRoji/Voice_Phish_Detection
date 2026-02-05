# aiml/inference.py

from pathlib import Path
import whisper
import torch

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

    try:
        # Try with FFmpeg first
        result = model.transcribe(
            str(audio_path),
            language="en",
            fp16=False  # CPU-safe, deployment-safe
        )
    except FileNotFoundError as e:
        # If FFmpeg is not found, load audio manually using librosa
        import librosa
        import numpy as np
        
        print("[WARN] FFmpeg not found, using librosa for audio loading")
        audio, sr = librosa.load(str(audio_path), sr=16000, mono=True)
        
        # Convert to torch tensor and normalize
        audio = torch.from_numpy(audio).float()
        
        result = model.transcribe(
            audio,
            language="en",
            fp16=False
        )

    text = result.get("text", "")
    return text.strip()
