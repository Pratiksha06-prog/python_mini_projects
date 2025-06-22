import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def talk(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to the user's voice and return the text."""
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        voice = listener.listen(source)
    try:
        command = listener.recognize_google(voice)
        command = command.lower()
        print("You said:", command)
    except:
        command = ""
    return command

def run_assistant():
    command = listen()

    if "hello" in command:
        talk("Hello! How can I help you?")
    
    elif "your name" in command:
        talk("I am your Python voice assistant.")
    
    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk("The time is " + time)

    elif "search for" in command:
        topic = command.replace("search for", "")
        talk("Searching for " + topic)
        pywhatkit.search(topic)

    else:
        talk("Sorry, I can't hear you.")

# Run the assistant
run_assistant()
