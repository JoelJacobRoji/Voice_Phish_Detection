# aiml/audio_features.py
import librosa
import numpy as np

def extract_audio_features(audio_path):
    y, sr = librosa.load(audio_path, sr=None)

    pitch = np.mean(librosa.yin(y, fmin=75, fmax=300))
    energy = np.mean(librosa.feature.rms(y=y))
    tempo = librosa.beat.tempo(y=y, sr=sr)[0]

    return {
        "pitch": float(pitch),
        "energy": float(energy),
        "tempo": float(tempo)
    }
