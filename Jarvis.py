# --- JARVIS AI Assistant ---
from stt import speak, engine
from sr import take_command
from LLM import get_llm_response
from dateandtime import get_datetime
from system_info import get_battery_status, get_cpu_usage, get_memory_usage
from ope_function import open_application , open_website 

def main():
    """Main program loop"""
    speak("I am JARVIS. How may I assist you today?")
    
    while True:
        query = take_command()
        
        # Skip if no valid input
        if query == "None":
            continue
        
        # Exit commands
        if any(word in query for word in ['exit', 'quit', 'stop', 'bye', 'shutdown', 'goodbye']):
            speak("Goodbye Sir. Have a wonderful day.")
            break
        
        # Greetings
        elif query.strip() in ['hello', 'hi', 'hey']:
            speak("Hello Sir! How can I help you?")
            continue
        
        elif 'how are you' in query or 'how r u' in query:
            speak("I'm functioning optimally, Sir. Ready to assist you.")
            continue
        
        elif 'your name' in query or 'who are you' in query:
            speak("I am JARVIS, your personal AI assistant, Sir.")
            continue
        elif 'time' in query or 'date' in query:
            current_datetime = get_datetime()
            speak(f"The current time is : {current_datetime}")
            continue
        elif 'battery' in query:
            battery_status = get_battery_status()
            speak(battery_status)

        elif 'cpu' in query or 'processor' in query:
            cpu_status = get_cpu_usage()
            speak(cpu_status)

        elif 'memory' in query or 'ram' in query:
            memory_status = get_memory_usage()
            speak(memory_status)

        elif 'open' in query or 'launch' in query or 'start' in query:
            if any(site in query for site in open_website.SITE_MAP.keys()):
                speak(open_website(query))
            elif any(app in query for app in open_application.apps.keys()):
                speak(open_application(query))
            else:
                speak("Sir, please specify what you want me to open.")
    
             
        
        # LLM conversational response for everything else
        print("💭 Consulting my intelligence core...")
        ai_response = get_llm_response(query)
        speak(ai_response)

# --- Program Entry Point ---
if __name__ == "__main__":
    main()