import speech_recognition as sr
import webbrowser
import pyttsx3
import pyjokes
import time
import os
import requests

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Speak the given text using the TTS engine."""
    engine.say(text)
    engine.runAndWait()

def ai_process(chat):
    """
    Send a prompt to the local phi AI model and return the response.
    The model acts as a virtual assistant named Jarvis.
    """
    response = requests.post(
        'http://localhost:11434/api/generate',
        json={
            'model': 'phi',
            'system': 'You are a virtual assistant named Jarvis',
            'prompt': chat,
            'stream': False
        }
    )
    print(response.json()['response'])
    return response.json()['response']

def search(query):
    """
    Perform a Google search for the given query.
    """
    query = query.replace("search for","")
    try:
        speak(f"Searching for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")
    except Exception as e:
        speak("Sorry, I could not perform the search.")
        print(f"Error: {e}")
        search(query)

def process_command(c):
    """
    Process the user's command and perform the corresponding action.
    """
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
        
    elif "open youtube" in c.lower():
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
        
    elif "open github" in c.lower():
        speak("Opening GitHub")
        webbrowser.open("https://www.github.com")
        
    elif "open instagram" in c.lower():
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
        
    elif "open chat gpt" in c.lower():
        speak("Opening ChatGPT")
        webbrowser.open("https://chat.openai.com")
        
    elif "tell me a joke" in c.lower():
        # Get a random joke and speak it
        joke = pyjokes.get_joke()
        speak(joke)

    elif "search" in c.lower():
        # Perform a Google search
        search(c)
        
    elif "what time" in c.lower():
        # Tell the current time
        current_time = time.strftime("%H:%M")
        speak(f"The current time is {current_time}")
        
    elif "play music" in c.lower():
        # Play music on YouTube based on the query
        speak("Playing music")
        q = c.replace("play music", "")
        webbrowser.open(f"https://www.youtube.com/results?search_query={q}")
        
    elif "open" in c.lower():
        # Try to open a local application
        app = c.replace("open", "").strip()
        speak(f"Opening {app}")
        try:
            os.system(f"start {app}")
        except Exception as e:
            speak(f"Sorry, I could not open {app}.")
            print(f"Error: {e}")
    else:
        # If command is not recognized, use the AI model to respond
        try:
            data = ai_process(c.lower())
            speak(data.lower())
            command = c.lower()
            while command.lower() != "ok":
                with sr.Microphone() as source:
                    print("AI Listening...")
                    audio = r.listen(source, timeout=3, phrase_time_limit=6)
                    command = r.recognize_google(audio)
                    print(command)
                final = ai_process(command.lower())
                speak(final.lower())
        except Exception as e:
            pass

if __name__ == "__main__": 
    # Main loop to keep Jarvis running and listening for commands
    speak("Initializing Jarvis.....")
    Active = True
    while Active:
        r = sr.Recognizer()
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source , timeout=2 , phrase_time_limit=3)
            word = r.recognize_google(audio)
            print(word)
            if "jarvis" in word.lower():
                # If wake word detected, listen for the next command
                speak("Yes sir")
                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = r.listen(source, timeout=3, phrase_time_limit=6)
                    command = r.recognize_google(audio)
                    print(command)
                    process_command(command) 
            elif "shutdown" in word.lower():
                # If shutdown command detected, exit the loop
                speak("Goodbye sir")
                Active = False
        except Exception as e:
            pass

