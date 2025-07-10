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


...
### 🧠 Unlock Full AI Potential (Optional)

To enable Jarvis to answer any question using a powerful AI model, you can use [Gemini AI](https://ai.google.dev/gemini-api/docs/quickstart) from Google.

**Steps:**

1. **Get a Gemini API Key**  
   - Sign up and generate an API key from [Google AI Studio](https://makersuite.google.com/app/apikey).

2. **Set Up Your API Key**  
   - Create a `.env` file in your project directory.
   - Add your Gemini API key like this:
     ```
     api_key=YOUR_GEMINI_API_KEY
     ```

3. **Install Requirements**  
   - Make sure you have installed all dependencies:
     ```bash
     pip install -r requirement.txt
     ```

4. **Run Jarvis**  
   - Now, when you ask Jarvis any question it doesn't recognize as a command, it will use Gemini AI to answer.

---

**Note:**  
- Gemini AI is only required if you want Jarvis to answer general questions using AI.  
- For basic voice commands and web automation, Gemini AI is not required.