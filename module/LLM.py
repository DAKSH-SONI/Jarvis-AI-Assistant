from google import genai
import os
# --- LLM Setup (Gemini 2.5) ---
LLM_MODEL = 'gemini-2.5-flash'
try:
    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
except Exception as e:
    print(f"Error initializing Gemini client: {e}")
    client = None

def get_llm_response(prompt):
    """Send user prompt to Gemini model and return text response"""
    if not client:
        return "I cannot connect to my intelligence core right now. Check my API configuration."
    
    system_prompt = (
    "You are Jarvis concise, confident, mildly witty, speaks in short declarative sentences"
    "Avoid long paragraphs. Use precise technical vocabulary if asked about tech."
    "When answering, keep sentences to 6 to 12 words and include one short pause every 8 to 12 words for effect."
    "Do not use contractions."
    )

    try:
        response = client.models.generate_content(
            model=LLM_MODEL,
            contents=prompt,
            config=genai.types.GenerateContentConfig(
                system_instruction=system_prompt
            )
        )
        return response.text if hasattr(response, "text") else "No response text received."
    except Exception as e:
        return f"Sir, I encountered an error while processing that: {str(e)}"


