import requests

url = "http://localhost:8000/analyze-audio"
files = {"file": ("test.wav", open("test_audio.wav", "rb"), "audio/wav")}

print("Sending request...")
try:
    response = requests.post(url, files=files)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    if response.status_code == 200:
        print(f"JSON: {response.json()}")
except Exception as e:
    print(f"Error: {e}")
