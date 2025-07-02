import speech_recognition as sr
import webbrowser
import pyttsx3
import pyjokes

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def search(query):
    query = query.replace("search for","")
            
    try:
        speak(f"Searching for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")
    except Exception as e:
        speak("Sorry, I could not perform the search.")
        print(f"Error: {e}")
        search(query)

def process_command(c):
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
        joke = pyjokes.get_joke()
        speak(joke)
    elif "open" in c.lower():
        q = c.replace("open", "")
        speak(f"Opening {q}")
        webbrowser.open(f"https://www.{q.split()[0]}")
    elif "search" in c.lower():
        search(c)
        
if __name__ == "__main__": 
    speak("Initializing Jarvis.....")
    while True:
        
        r = sr.Recognizer()
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source , timeout=2 , phrase_time_limit=3)
            word = r.recognize_google(audio)
            print(word)
            if "jarvis" in word.lower():
                speak("Yes sir")
                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = r.listen(source, timeout=3, phrase_time_limit=5)
                    command = r.recognize_google(audio)
                    print(command)
                    process_command(command) 
        except Exception as e:
            print("Error {0}" .format(e))
                    
        