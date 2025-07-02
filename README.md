# Jarvis 🧠🎙️ — Python Voice Assistant

**Jarvis** is a voice-controlled personal assistant built with Python. It listens to your voice commands and performs simple tasks — like opening websites — directly in your browser. This is an early version of the assistant and will be expanded in the future with more capabilities.

---

## 🎯 Features

- 🎤 Voice input using microphone
- 🔊 Voice feedback using text-to-speech
- 🌐 Open websites and perform basic browser tasks
- 🐍 Written in pure Python (no external APIs)
- ⚡ Lightweight and easy to run

---

## 🛠️ Technologies Used

- `speech_recognition` – For capturing and understanding voice input
- `pyttsx3` – For text-to-speech voice output
- `webbrowser` – To open URLs in your default browser
- `datetime`, `os`, `time` – Built-in Python modules for additional tasks

---

## 🖥️ How It Works

1. Jarvis listens through your microphone.
2. Recognizes your speech using offline/local recognition.
3. Matches the command and executes a relevant Python function.
4. Responds with a spoken confirmation (e.g., "Opening YouTube").

Example voice commands:
- "Open Google"
- "Open YouTube"
- "What time is it?"
- "Search { something }" to search any query on google  

---

## 📦 Requirements

Before running the assistant, install the following libraries:

```bash
pip install -r requirement.txt