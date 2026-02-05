# Audio Call Analyzer - WORKING! ✅

## 🎯 Quick Start (Easy Way)

**Just double-click `START.bat` - it will:**
1. Start the backend server (port 8000)
2. Start the frontend server (port 3000)  
3. Open your browser automatically

**Then test by uploading an audio file!**

---

## What Was Fixed

### Main Issue Found & Fixed:
**The frontend was using `window.location.hostname` which is EMPTY when opening HTML from file:// protocol!**

1. ✅ Fixed BACKEND_URL to always use `http://localhost:8000`
2. ✅ Created proper HTTP server for frontend (no more file:// issues)
3. ✅ Added FFmpeg fallback using librosa for audio loading
4. ✅ Created convenient startup script (START.bat)
5. ✅ Enhanced error messages and logging

---

## Manual Start (If you prefer)

### Start Backend:
```powershell
.\.venv\Scripts\python.exe -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000
```

### Start Frontend:
```powershell
.\.venv\Scripts\python.exe serve_frontend.py
```

### Open Browser:
Go to: **http://localhost:3000/index.html**

---

## Current Status

✅ Backend Server: http://localhost:8000  
✅ Frontend Server: http://localhost:3000  
✅ Audio Processing: Working with librosa fallback  
✅ ML Model: Trained and loaded  

---

## How to Test

1. **Open** http://localhost:3000/index.html (or use START.bat)
2. Click **"Select the audio file"** button
3. Choose any audio file (.wav, .mp3, .m4a, .ogg)
4. Click **"Analyze Audio"**
5. Wait 15-30 seconds for analysis (Whisper processing)
6. See results with:
   - Risk Level (High/Medium/Low)
   - Risk Score percentage
   - Detected scam phrases
   - Full transcript

---

## Test Audio Files

You can test with:
- Any voice recording from your phone
- WhatsApp audio messages exported as audio files
- Any .wav or .mp3 file with speech
- Record a message saying scam keywords like "OTP", "urgent", "bank account"

---

## Important Notes

⚠️ **First audio analysis will be slow (15-30 seconds)** - Whisper model loading  
⚠️ You'll see "[WARN] FFmpeg not found, using librosa" - **this is normal and working!**  
⚠️ Make sure both servers are running before testing  

---

## Check Servers

Backend health: http://localhost:8000/health  
Frontend: http://localhost:3000/index.html

---

## Troubleshooting

**If it still doesn't work:**
1. Close all browser tabs
2. Stop all Python processes
3. Run START.bat again
4. Wait for both servers to start
5. Try with a simple .wav file first

**Check browser console (F12)** - you should see:
- "Sending request to: http://localhost:8000/analyze-audio"
- Response logs
