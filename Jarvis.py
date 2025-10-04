import pyttsx3
import speech_recognition as sr
from google import genai
import os
import pyttsx3
import webbrowser # Added import for webbrowser
import subprocess # Added import for subprocess to open apps
# --- SITE MAP (New Dictionary for all Web Shortcuts) ---
SITE_MAP = {
    # Original Sites
    "youtube": "https://www.youtube.com",
    "wikipedia": "https://www.wikipedia.com",
    "google": "https://www.google.com",

    # Social Media
    "facebook": "https://www.facebook.com",
    "instagram": "https://www.instagram.com",
    "twitter": "https://www.twitter.com",
    "linkedin": "https://www.linkedin.com",

    # Shopping & Affiliate
    "amazon": "https://www.amazon.in",
    "flipkart": "https://www.flipkart.com",
    "meesho": "https://www.meesho.com",
    "amazon associates": "https://affiliate-program.amazon.in",
    "iphone": "https://www.apple.com",

    # Entertainment & Streaming
    "netflix": "https://www.netflix.com",
    "spotify": "https://www.spotify.com",

    # Developer & Education
    "github": "https://www.github.com",

    # Communication & Tools
    "gmail": "https://mail.google.com",
    "chatgpt": "https://chat.openai.com"
}

apps = {
    "calculator": "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App",
    "spotify": "SpotifyAB.SpotifyMusic_zpdnekdrzrea0!Spotify",
    "camera": "Microsoft.WindowsCamera_8wekyb3d8bbwe!App",
    "whatsapp" : "5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App",
    "github desktop" : "com.squirrel.GitHubDesktop.GitHubDesktop",
    "telegarm" : "Telegram.TelegramDesktop",
    "notepad" : "Microsoft.WindowsCamera_8wekyb3d8bbwe!App",
    "google chrome" :  "Chrome",
    "Canva" : "com.canva.CanvaDesktop",
    "Brave" :  "Brave"
}

# --- END SITE MAP ---
# # --- LLM Setup (Gemini 2.5) ---
# Ensure you have set the environment variable for the API key before running the script
LLM_MODEL = 'gemini-2.5-flash'
try:
    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

    # Choose a fast and capable model for conversation
except Exception as e:
    print(f"Error initializing Gemini client: {e}")
    client = None
# --- End LLM Setup ---

def get_llm_response(prompt):
    # send the usser prompt to the gimini model and return the text response
    if not client:
        return "I cannot connect to my intelligence core right now. Check my API configuration."
    system_prompt =( "You are J.A.R.V.I.S., a sophisticated, polite, and witty AI assistant. "
        "Your responses should be concise and helpful. Refer to the user as 'Sir'."
    )
    try:
        response = client.models.generate_content(
            model = LLM_MODEL,
            contents = prompt,
            config = genai.types.GenerateContentConfig(
                system_instruction =system_prompt
            )
        )    
        return response.text
    except Exception as e:
        return f"sir ,i encountered a network error while processing that : {e}"
    
# --- TTS Setup (J.A.R.V.I.S. Voice) ---

#init the pyttsx3 text to speech engine
engine = pyttsx3.init('sapi5')  #sapi5 is a microsoft speech api

voices = engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[0].id) #changing index changes voices.
engine.setProperty('rate', 150) #setting up new voice rate (faster)
engine.setProperty('volume', 1.0) #setting up volume level  between
def speak(audio):
    "jarvis will speak the audio passed to this function"
    engine.say(audio)
    print(f"Jarvis :  {audio}")
    engine.runAndWait()

 #test the speak function 
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.... ")
        r.pause_threshold = 1 #seconds of non speaking silence
        r.energy_threshold = 300 #minimum audio energy to consider for recording
        audio = r.listen(source,timeout=5 , phrase_time_limit=10) #listen for the first phrase and extract it into audio data
    try:    
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in') #using google for speech recognition
        print(f"User said: {query}\n") #user query will be printed
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please say that again.")
        return "None"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return "None"
    return query.lower() #converting the query into lower case  
def main():
    def open_app(app_name):
        try:
            if app_name in apps:
                app_id = apps[app_name]
                subprocess.Popen(f"start shell:AppsFolder\\{app_id}", shell=True)
                speak(f"Opening {app_name}, sir.")
            else:
                speak(f"Sorry sir, {app_name} is not in my list.")
        except Exception as e:
            speak(f"Sorry sir, I couldn’t open {app_name}.")
            print(e)   
    speak("I am Jarvis, How can I help you today?") 
    while True:
        query = take_command() #calling the take_command function
 
        #logic for executing tasks based on query
        if query == "None":
            continue
         # B. Universal Website/Application Commands (using the new SITE_MAP)
        # Check if the query contains "open" or "go to" followed by any site key
        site_opened = False
        if 'open' in query or 'go to' in query or 'launch' in query:
            for keyword, url in SITE_MAP.items():
                if keyword in query:
                    speak(f"Opening {keyword}, Sir.")
                    webbrowser.open(url)
                    site_opened = True
                    break
        if site_opened:
            continue # Skip to the next loop iteration
        elif "open" in query:
            words = query.split()
            try:
                app_name = " ".join(words[words.index("open")+1:]).lower()
                open_app(app_name)
            except:
                speak("Please tell me which app to open, sir.")
                opened = True
                break

        elif'exit' in query or 'quit' in query or 'stop' in query or 'bye' in query:
            speak("Goodbye! Have a great day.")
            break
        elif 'hello' in query.strip() or 'hi' in query.strip():
            speak("Hello sir! how can help you?")
        elif 'how are you' in query or "how r u" in query:
            speak("I am just a program, but I'm work for you?")
        elif 'your name' in query:
            speak("I am Jarvis, your personal AI assistant.")
          # --- The New LLM Conversational Logic ---
        else:
            print("Sending query to LLM...")
            ai_response = get_llm_response(query)
            speak(ai_response)
    
# --- Program Entry Point (Best Practice) ---
if __name__ == "__main__":
    main()
    