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
- "Open GitHub"
- "Open Instagram"
- "Open Chat GPT"
- "Tell me a joke"
- "What time is it?"
- "Play music despacito"
- "Search for Python tutorials"
- "Open notepad"
- "Open calculator"
- "Shutdown"
- "Ask AI what is the capital of France?"
- "Search weather in London"
- "Play music Alan Walker"
- "Search for latest news"
- "Open command prompt"
- "Open paint"
- "Search for how to make pizza"
- "What is the date today?"

---

## 📦 Requirements

Before running the assistant, install the following libraries:

```bash
pip install -r requirement.txt
```


---


### 🧠 Unlock Full AI Potential (Optional)

To enable Jarvis to answer any question using a local AI model, you need to install [Ollama](https://ollama.com/) and run the `phi` model locally on your system.

**Steps:**

1. **Install Ollama**  
   Download and install Ollama from [https://ollama.com/download](https://ollama.com/download) for your operating system.

2. **Pull the Phi Model**  
   Open your terminal and run:
   ```bash
   ollama pull phi
   ```

3. **Start the Ollama Service**  
   Make sure Ollama is running. By default, it listens on `http://localhost:11434`.

4. **Run Jarvis**  
   Now, when you ask Jarvis any question it doesn't recognize as a command, it will use the local AI model to answer.

---

**Note:**  
- Ollama and the phi model are only required if you want Jarvis to answer general questions using AI.  
- For basic voice commands and web automation, Ollama is not required.