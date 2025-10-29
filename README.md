Jarvis AI Assistant

A personal AI-powered desktop assistant built with Python. Jarvis automates common system tasks, opens websites and applications, provides real-time system information, and intelligently answers user queries using a built-in LLM (Gemini 2.5 Flash) — all through natural voice interaction.

Project Overview

Jarvis is designed as a modular, extensible, and intelligent personal assistant.
It can perform day-to-day operations such as opening system applications, browsing websites, and retrieving information using a conversational interface.
The system integrates speech recognition, text-to-speech synthesis, and a large language model to create a seamless user experience.

Key Features

Smart Task Automation

Opens websites (e.g., YouTube, Google, Wikipedia).
Launches system applications (e.g., Notepad, Calculator, Command Prompt).

AI Query Handling (Gemini 2.5 Flash)

Integrates the Gemini 2.5 Flash LLM for intelligent query answering.

Provides fast, context-aware responses through text or voice.

Voice Interaction

Utilizes pyttsx3 for text-to-speech output.

Configured for a natural-sounding male voice.

System Information Monitoring

Displays battery percentage, CPU usage, and memory statistics using the psutil module.

Modular Architecture

Each function (e.g., speech input, voice output, task automation, LLM interaction, system utilities) is developed as a separate module.

Enhances readability, maintainability, and scalability.

Technology Stack
Component	Library / Tool	Description
Voice Input	speech_recognition	Captures and processes spoken commands
Voice Output	pyttsx3	Generates speech output with customizable voices
AI Model	google.genai (Gemini 2.5 Flash)	Handles complex queries and conversational responses
System Operations	os, subprocess, psutil, webbrowser	Manages app and website control
Modular Design	Python Packages	Enables structured and maintainable codebase
Future Enhancements

Add GUI dashboard for visual interaction.

Integrate OpenCV for facial recognition and emotion detection.

Extend LLM capabilities for context retention and personalized responses.

Include task scheduling and notification system.