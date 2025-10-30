# 🤖 Jarvis AI Assistant

A personal **AI-powered desktop assistant** built with **Python**.  
Jarvis automates system tasks, opens websites and applications, provides real-time system stats, and answers queries using **Gemini 2.5 Flash LLM** — all through **natural voice interaction**.

---

## 🧭 Project Overview

Jarvis is a **modular**, **extensible**, and **intelligent** voice-based assistant designed for desktop environments.  
It performs day-to-day tasks such as:

- Opening apps and websites  
- Retrieving system information  
- Providing intelligent responses using Gemini LLM  
- Interacting through speech input and output  

Each component (speech, AI, system utilities, automation) is designed as a **separate Python module**, ensuring clarity and scalability.

---

## ⚙️ Key Features

### 🧠 Smart Task Automation
- Opens popular websites like **YouTube**, **Google**, **Wikipedia**
- Launches system applications such as **Notepad**, **Calculator**, **Command Prompt**
- Uses Python’s built-in modules for OS-level automation

### 💬 AI Query Handling (Gemini 2.5 Flash)
- Integrated **Google Gemini 2.5 Flash LLM**
- Handles general and technical questions intelligently
- Provides **fast**, **context-aware**, and **natural responses**

### 🗣️ Voice Interaction
- **Speech-to-Text:** via `speech_recognition`  
- **Text-to-Speech:** via `pyttsx3`  
- Fully hands-free experience with natural speech synthesis

### 🧩 System Information Monitoring
- Displays real-time **CPU**, **RAM**, and **battery** stats  
- Uses `psutil` for precise system metrics

### 🧱 Modular Architecture
- Every functionality is a **separate module**:
  - `stt.py` → Speech to Text  
  - `LLM.py` → Large Language Model integration  
  - `system_info.py` → System stats  
  - `ope_function.py` → Task automation  
  - `dateandtime.py` → Date and time utilities  
- Makes the code easy to read, maintain, and extend.

---

## 🧰 Technology Stack

| Component | Library / Tool | Description |
|------------|----------------|-------------|
| **Voice Input** | `speech_recognition` | Captures and converts spoken commands into text |
| **Voice Output** | `pyttsx3` | Generates natural voice responses (offline TTS) |
| **AI Model** | `google.genai` (Gemini 2.5 Flash) | Handles intelligent and conversational responses |
| **System Operations** | `os`, `subprocess`, `psutil`, `webbrowser` | Automates applications and retrieves system info |
| **Architecture** | Custom Python Modules | Ensures modular, scalable design |

---

## 🧠 Why These Libraries?

- **speech_recognition:** Accurate speech input handling  
- **pyttsx3:** Offline text-to-speech with customizable voices  
- **psutil:** System monitoring (battery, CPU, RAM)  
- **os & subprocess:** Core automation for apps and system commands  
- **webbrowser:** Quick and lightweight URL launching  
- **google.genai:** Integrates Gemini LLM for intelligent query responses  

---

## 🚀 Future Enhancements

- 🪟 Add **GUI dashboard** for visual interaction  
- 👁️ Integrate **OpenCV** for facial recognition & emotion detection  
- 🧠 Improve **context retention** for personalized responses  
- ⏰ Add **task scheduling** and **reminder system**  
- 💬 Multi-language voice support  

---

## 🪄 Example Command Flow

**User:** “Jarvis, open YouTube”  
**Jarvis:** *(launches browser and responds with voice)* “Opening YouTube, sir.”  

**User:** “What’s my CPU usage?”  
**Jarvis:** “Your CPU is currently running at 43 percent.”  

**User:** “Tell me about black holes.”  
**Jarvis:** *(Gemini LLM responds with natural explanation)*  

---

## 🧑‍💻 Setup & Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Jarvis-AI-Assistant.git
   cd Jarvis-AI-Assistant
