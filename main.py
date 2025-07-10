import speech_recognition as sr
import webbrowser
import pyttsx3
import pyjokes
import time
import os
from dotenv import load_dotenv, find_dotenv, get_key
import google.generativeai as genai


# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def ai_process(chat):
    load_dotenv()
    api_key = get_key(find_dotenv(), "api_key")

    # Configure API key
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(f"{chat} respond in a short and concise manner")


    print(response.text)
    return response.text

def search(query):
    query = query.replace("search for", "")
    try:
        speak(f"Searching for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")
    except Exception as e:
        speak("Sorry, I could not perform the search.")
        print(f"Error: {e}")

def process_command(c):
    c = c.lower()
    r = sr.Recognizer()

    if "open google" in c:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in c:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open github" in c:
        speak("Opening GitHub")
        webbrowser.open("https://www.github.com")

    elif "open instagram" in c:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")

    elif "open chat gpt" in c:
        speak("Opening ChatGPT")
        webbrowser.open("https://chat.openai.com")

    elif "tell me a joke" in c:
        joke = pyjokes.get_joke()
        speak(joke)

    elif "search" in c:
        search(c)

    elif "what time" in c:
        current_time = time.strftime("%H:%M")
        speak(f"The current time is {current_time}")

    elif "play music" in c:
        speak("Playing music")
        q = c.replace("play music", "")
        webbrowser.open(f"https://www.youtube.com/results?search_query={q}")

    elif "open" in c:
        app = c.replace("open", "").strip()
        speak(f"Opening {app}")
        try:
            os.system(f"start {app}")
        except Exception as e:
            speak(f"Sorry, I could not open {app}.")
            print(f"Error: {e}")
    else:
        # If not matched, use AI response
        data = ai_process(c)
        speak(data)

        while True:
            with sr.Microphone() as source:
                print("AI Listening for next input... Say 'ok' to stop.")
                try:
                    audio = r.listen(source, timeout=3, phrase_time_limit=5)
                    command = r.recognize_google(audio)
                    print("You said:", command)
                    if command.lower() == "ok":
                        break
                    else:
                        reply = ai_process(command)
                        speak(reply)
                except:
                    break

if __name__ == "__main__":
    speak("Initializing Jarvis.....")
    Active = True
    while Active:
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=3)
            word = recognizer.recognize_google(audio)
            print("Heard:", word)

            if "jarvis" in word.lower():
                speak("Yes sir")
                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = recognizer.listen(source, timeout=4, phrase_time_limit=6)
                    command = recognizer.recognize_google(audio)
                    print("Command:", command)
                    process_command(command)
            
            elif "shutdown" in word.lower():
                speak("Goodbye sir")
                os.system("shutdown /s /t 1")
                Active = False

        except Exception as e:
            pass
