"""
Complete system test - verifies all components are working
"""
import requests
import time

print("=" * 60)
print("  AUDIO CALL ANALYZER - SYSTEM TEST")
print("=" * 60)
print()

# Test 1: Backend Health
print("[1/4] Testing Backend Health...")
try:
    response = requests.get("http://localhost:8000/health", timeout=5)
    if response.status_code == 200:
        print("  ✅ Backend is healthy:", response.json())
    else:
        print(f"  ❌ Backend returned: {response.status_code}")
        exit(1)
except Exception as e:
    print(f"  ❌ Backend not accessible: {e}")
    print("  → Make sure backend is running on port 8000")
    exit(1)

# Test 2: Frontend Server
print("\n[2/4] Testing Frontend Server...")
try:
    response = requests.get("http://localhost:3000/index.html", timeout=5)
    if response.status_code == 200:
        print(f"  ✅ Frontend is serving (size: {len(response.content)} bytes)")
    else:
        print(f"  ❌ Frontend returned: {response.status_code}")
        exit(1)
except Exception as e:
    print(f"  ❌ Frontend not accessible: {e}")
    print("  → Make sure frontend server is running on port 3000")
    exit(1)

# Test 3: Audio Analysis API
print("\n[3/4] Testing Audio Analysis API...")
try:
    files = {"file": ("test.wav", open("test_audio.wav", "rb"), "audio/wav")}
    response = requests.post("http://localhost:8000/analyze-audio", files=files, timeout=30)
    
    if response.status_code == 200:
        result = response.json()
        print("  ✅ Audio analysis successful!")
        print(f"     - Risk Level: {result.get('risk_level', 'N/A')}")
        print(f"     - Risk Score: {result.get('risk_score', 0)}%")
        print(f"     - Has Transcript: {'Yes' if result.get('transcript') else 'No (silent audio)'}")
    else:
        print(f"  ❌ Analysis failed: {response.status_code}")
        print(f"     Response: {response.text}")
        exit(1)
except Exception as e:
    print(f"  ❌ Analysis error: {e}")
    exit(1)

# Test 4: Summary
print("\n[4/4] System Status Summary")
print("  ✅ Backend Server:  http://localhost:8000")
print("  ✅ Frontend Server: http://localhost:3000")
print("  ✅ API Endpoint:    /analyze-audio")
print("  ✅ All systems operational!")

print("\n" + "=" * 60)
print("  🎉 ALL TESTS PASSED!")
print("=" * 60)
print("\n📱 Open your browser to: http://localhost:3000/index.html")
print("🎤 Upload an audio file and test the analyzer!")
print()
