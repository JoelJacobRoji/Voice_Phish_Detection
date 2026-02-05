# Audio Call Analyzer - Installation Guide

## 📋 Table of Contents
- [System Requirements](#system-requirements)
- [Prerequisites](#prerequisites)
- [Installation Steps](#installation-steps)
- [Running the Application](#running-the-application)
- [Troubleshooting](#troubleshooting)
- [Project Structure](#project-structure)

---

## 💻 System Requirements

- **Operating System:** Windows 10/11 (Linux/Mac compatible with minor adjustments)
- **Python:** Version 3.8 or higher (3.10+ recommended)
- **RAM:** Minimum 4GB (8GB+ recommended for Whisper model)
- **Disk Space:** ~2GB for dependencies and models
- **Internet:** Required for initial model download

---

## 🔧 Prerequisites

### 1. Python Installation
Ensure Python is installed and added to PATH:
```powershell
python --version
```
Should output: `Python 3.x.x`

**Download Python:** https://www.python.org/downloads/

### 2. Git (Optional)
For cloning the repository:
```powershell
git --version
```

---

## 📦 Installation Steps

### Step 1: Navigate to Project Directory
```powershell
cd "d:\Hackathon\HCL GUVI 2026\New folder\Audio_Call_Analyzer"
```

### Step 2: Create Virtual Environment
```powershell
python -m venv .venv
```

This creates an isolated Python environment in the `.venv` folder.

### Step 3: Activate Virtual Environment

**On Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**On Windows (CMD):**
```cmd
.venv\Scripts\activate.bat
```

**On Linux/Mac:**
```bash
source .venv/bin/activate
```

You should see `(.venv)` prefix in your terminal.

### Step 4: Install Dependencies

**Install backend dependencies:**
```powershell
pip install -r backend/requirements.txt
```

This will install:
- FastAPI - Web framework
- Uvicorn - ASGI server
- OpenAI Whisper - Speech-to-text model
- Librosa - Audio processing
- Scikit-learn - Machine learning
- Pandas - Data manipulation
- PyTorch - Deep learning framework
- And other required packages

**Installation time:** ~5-10 minutes depending on internet speed

### Step 5: Prepare Data & Train Model

**Create artifacts directory:**
```powershell
mkdir aiml\artifacts -Force
```

**Train the text scam detection model:**
```powershell
python aiml\train_text_model.py
```

**Expected output:**
```
✅ Text scam model trained & saved
```

This creates:
- `aiml/artifacts/text_model.pkl` - Trained logistic regression model
- `aiml/artifacts/text_vectorizer.pkl` - TF-IDF vectorizer

**Training time:** ~10-30 seconds

---

## 🚀 Running the Application

### Method 1: Easy Startup (Recommended)

**Double-click:** `START.bat`

This automatically:
1. ✅ Starts backend server on port 8000
2. ✅ Starts frontend server on port 3000
3. ✅ Opens browser to http://localhost:3000/index.html

### Method 2: Manual Startup

**Terminal 1 - Start Backend:**
```powershell
.\.venv\Scripts\python.exe -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000
```

**Terminal 2 - Start Frontend:**
```powershell
.\.venv\Scripts\python.exe serve_frontend.py
```

**Then open browser to:**
```
http://localhost:3000/index.html
```

### Verify Installation

**Run system test:**
```powershell
python test_system.py
```

**Expected output:**
```
============================================================
  AUDIO CALL ANALYZER - SYSTEM TEST
============================================================

[1/4] Testing Backend Health...
  ✅ Backend is healthy: {'status': 'ok', 'service': 'audio-scam-analyzer'}

[2/4] Testing Frontend Server...
  ✅ Frontend is serving (size: 1506 bytes)

[3/4] Testing Audio Analysis API...
  ✅ Audio analysis successful!

[4/4] System Status Summary
  ✅ All systems operational!

============================================================
  🎉 ALL TESTS PASSED!
============================================================
```

---

## 🎯 Using the Application

### Upload and Analyze Audio

1. **Open browser:** http://localhost:3000/index.html
2. **Click:** "Select the audio file" button
3. **Choose:** Any audio file (.wav, .mp3, .m4a, .ogg)
4. **Click:** "Analyze Audio" button
5. **Wait:** 15-30 seconds for first analysis (Whisper model loading)
6. **View Results:**
   - Risk Level (High/Medium/Low)
   - Risk Score (0-100%)
   - Detected Scam Phrases
   - Full Transcript

### Supported Audio Formats
- ✅ WAV (.wav)
- ✅ MP3 (.mp3)
- ✅ M4A (.m4a)
- ✅ OGG (.ogg)

### Test Audio Files
Create test recordings saying:
- **Low Risk:** "Hello, this is a test message"
- **High Risk:** "Please share your OTP and bank account details urgently"

---

## 🔍 Troubleshooting

### Issue 1: "Module not found" Error

**Solution:**
```powershell
# Ensure virtual environment is activated
.\.venv\Scripts\Activate.ps1

# Reinstall dependencies
pip install -r backend/requirements.txt
```

### Issue 2: Backend Not Starting

**Check if port 8000 is in use:**
```powershell
netstat -ano | findstr :8000
```

**Kill process if needed:**
```powershell
taskkill /PID <PID_NUMBER> /F
```

### Issue 3: Frontend Not Loading

**Verify frontend server is running:**
```powershell
# Check if port 3000 is listening
netstat -ano | findstr :3000
```

**Restart frontend server:**
```powershell
.\.venv\Scripts\python.exe serve_frontend.py
```

### Issue 4: "Failed to analyze audio"

**Check backend logs in terminal for errors.**

**Common causes:**
- Model files missing → Run `python aiml\train_text_model.py`
- Audio file format unsupported → Use .wav or .mp3
- Insufficient memory → Close other applications

### Issue 5: Slow Analysis

**First run is always slow (~30 seconds) because:**
- Whisper model downloads (~139MB)
- Model loads into memory
- Audio processing initialization

**Subsequent analyses are faster (~10-15 seconds).**

### Issue 6: FFmpeg Warning

**You may see:**
```
[WARN] FFmpeg not found, using librosa for audio loading
```

**This is NORMAL!** The application uses librosa as a fallback and works perfectly.

**To remove warning (optional):**
1. Download FFmpeg: https://ffmpeg.org/download.html
2. Add to system PATH
3. Restart application

---

## 📁 Project Structure

```
Audio_Call_Analyzer/
├── aiml/                      # AI/ML modules
│   ├── artifacts/             # Trained models (generated)
│   │   ├── text_model.pkl
│   │   └── text_vectorizer.pkl
│   ├── data/                  # Training datasets
│   │   └── sms_spam.csv
│   ├── audio_features.py      # Audio feature extraction
│   ├── inference.py           # Whisper transcription
│   ├── keyword_engine.py      # Scam keyword detection
│   ├── preprocessing.py       # Text cleaning
│   ├── scam_analyzer.py       # Main analysis pipeline
│   └── train_text_model.py    # Model training script
│
├── backend/                   # FastAPI backend
│   ├── app/
│   │   ├── __init__.py
│   │   └── main.py           # API endpoints
│   └── requirements.txt       # Python dependencies
│
├── frontend/                  # Web interface
│   ├── index.html            # Main page
│   ├── script.js             # Frontend logic
│   └── style.css             # Styling
│
├── .venv/                     # Virtual environment (created)
├── temp/                      # Temporary audio files (auto-created)
│
├── START.bat                  # Quick start script
├── serve_frontend.py          # Frontend HTTP server
├── test_system.py            # System verification test
├── test_analysis.py          # Analysis test
├── test_api.py               # API test
│
├── INSTALL.md                # This file
├── TESTING_GUIDE.md          # Testing instructions
└── SYSTEM_WORKING.md         # Fix documentation
```

---

## 🔐 Security Notes

### Development Environment
- CORS is set to allow all origins (`*`) for development
- Change this in production: `backend/app/main.py`

### Production Deployment
Before deploying to production:

1. **Update CORS settings:**
```python
# In backend/app/main.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],  # Specific domain
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
```

2. **Add authentication:**
- Implement API keys or OAuth
- Rate limiting
- Input validation

3. **Use HTTPS:**
- SSL certificate required
- Secure backend endpoints

4. **Environment variables:**
- Move sensitive config to `.env` files
- Never commit credentials

---

## 📊 System Architecture

```
┌─────────────────┐
│   Frontend      │
│  (Port 3000)    │
│  HTML/CSS/JS    │
└────────┬────────┘
         │ HTTP POST
         │ /analyze-audio
         ↓
┌─────────────────┐
│   Backend       │
│  FastAPI        │
│  (Port 8000)    │
└────────┬────────┘
         │
         ↓
┌─────────────────────────────────┐
│      AI/ML Pipeline             │
├─────────────────────────────────┤
│ 1. Whisper (Speech-to-Text)    │
│ 2. Text Preprocessing           │
│ 3. ML Model (Scam Detection)   │
│ 4. Keyword Engine               │
│ 5. Audio Features               │
│ 6. Risk Scoring                 │
└─────────────────────────────────┘
```

---

## 🔄 Update Instructions

### Update Dependencies
```powershell
pip install --upgrade -r backend/requirements.txt
```

### Retrain Model with New Data
1. Add new data to `aiml/data/sms_spam.csv`
2. Run training:
```powershell
python aiml\train_text_model.py
```

### Clear Cache
```powershell
# Remove temporary files
rmdir /s /q temp

# Clear Python cache
rmdir /s /q __pycache__
rmdir /s /q aiml\__pycache__
rmdir /s /q backend\app\__pycache__
```

---

## 🆘 Support & Contact

**Developed by:** Unsupervised Coders © 2026

**For issues:**
1. Check [TROUBLESHOOTING](#troubleshooting) section
2. Review [TESTING_GUIDE.md](TESTING_GUIDE.md)
3. Check browser console (F12) for errors
4. Review backend logs in terminal

---

## 📝 License

This project is part of HCL GUVI Hackathon 2026.

---

## ✅ Quick Checklist

Before running the application, ensure:

- [ ] Python 3.8+ installed
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip install -r backend/requirements.txt`)
- [ ] Model trained (`python aiml\train_text_model.py`)
- [ ] Backend server started (port 8000)
- [ ] Frontend server started (port 3000)
- [ ] Browser opened to http://localhost:3000/index.html

**If all checked, you're ready to analyze audio calls! 🎉**

---

## 🎓 How It Works

### 1. Audio Upload
User uploads audio file → Saved temporarily in `temp/` folder

### 2. Speech Recognition
Whisper model transcribes audio → Extracts text transcript

### 3. Text Analysis
- Clean and preprocess text
- TF-IDF vectorization
- Logistic regression classification

### 4. Keyword Detection
Scan transcript for scam-related keywords:
- OTP, password, bank account
- Urgent, immediately, suspended
- Wire transfer, gift card, lottery
- Police case, arrest, legal action

### 5. Audio Features
Extract voice characteristics:
- Pitch (frequency analysis)
- Energy (volume analysis)
- Tempo (speed analysis)

### 6. Risk Scoring
Combine scores with weights:
- ML Model: 50%
- Keywords: 30%
- Voice Features: 20%

### 7. Risk Level
- **Low:** Score < 40%
- **Medium:** Score 40-70%
- **High:** Score > 70%

---

**Installation Complete! 🚀**
