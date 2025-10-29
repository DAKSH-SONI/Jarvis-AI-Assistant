import speech_recognition as sr

def take_command():
    """Listen to microphone and return recognized speech as text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("🎧 Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        
        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=15)
        except sr.WaitTimeoutError:
            print("⏱️ Listening timed out.")
            return "None"
    
    try:
        print("🔍 Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"✅ User said: {query}\n")
        return query.lower()
    except sr.UnknownValueError:
        print("❌ Sorry, I didn't catch that.")
        return " "
    except sr.RequestError as e:
        print(f"❌ Speech recognition error: {e}")
        return " "