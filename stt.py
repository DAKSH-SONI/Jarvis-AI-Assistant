# --- TTS Setup (J.A.R.V.I.S. Voice) ---
import pyttsx3
engine = pyttsx3.init('sapi5')  # Microsoft Speech API

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Index 0 is typically male (David)
engine.setProperty('rate', 175)  # Slightly faster for more natural flow
engine.setProperty('volume', 1.0)

def speak(audio):
    """JARVIS speaks the provided text"""
    engine.say(audio)
    print(f"JARVIS: {audio}")
    engine.runAndWait()
