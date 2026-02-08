# aiml/inference.py

import os
from faster_whisper import WhisperModel

# --------------------------------------------------
# Load model once (CPU-only, deployment safe)
# --------------------------------------------------
MODEL_SIZE = "base"

model = WhisperModel(
    MODEL_SIZE,
    device="cpu",
    compute_type="int8"   # critical for low memory usage
)

# --------------------------------------------------
# Speech → Text
# --------------------------------------------------
def transcribe_audio(audio_path: str) -> str:
    if not os.path.exists(audio_path):
        raise FileNotFoundError("Audio file not found")

    segments, _ = model.transcribe(
        audio_path,
        beam_size=5,
        language="en"
    )

    transcript = " ".join(segment.text for segment in segments)
    return transcript.strip()
