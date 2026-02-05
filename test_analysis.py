import sys
sys.path.insert(0, '.')
from aiml.scam_analyzer import analyze_call

print("Testing audio analysis...")
try:
    result = analyze_call('test_audio.wav')
    print("\n✅ Analysis successful!")
    print(f"Result: {result}")
except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()
