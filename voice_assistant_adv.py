"""
Advanced Python Voice Assistant
Features are included:
Understands voice commands
Tells time
Searches Google
Gives weather updates
Answers general questions using Wikipedia
Saves reminders
Sends emails (Gmail)
Uses third-party APIs (OpenWeather)
"""

import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import requests
import wikipedia
import smtplib

# Initialize text-to-speech engine
engine = pyttsx3.init()

def talk(text):
    """Speak out the given text."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to voice input and return recognized text."""
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("The voice assistant is Listening...")
        voice = listener.listen(source)
    try:
        command = listener.recognize_google(voice)
        command = command.lower()
        print("You said that:", command)
    except:
        command = ""
    return command

def get_weather(city):
    """Fetch weather using OpenWeather API."""
    api_key = "your_openweather_api_key"  
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        return f"The weather in {city} is {weather} with {temp}°C temperature."
    else:
        return "Sorry, I couldn't find that city."

def send_email(to_email, subject, message):
    """Send an email using Gmail SMTP."""
    from_email = "your_email@gmail.com"
    password = "your_email_password"  # Use app password for security
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_email, password)
        email = f"Subject: {subject}\n\n{message}"
        server.sendmail(from_email, to_email, email)
        server.quit()
        talk("Email has been sent successfully.")
    except:
        talk("Sorry, I couldn't send the email.")

def save_reminder(task):
    """Save reminder in a text file."""
    with open("reminders.txt", "a") as file:
        file.write(task + "\n")
    talk("Reminder saved.")

def run_assistant():
    talk("Hello! I am your advanced voice assistant.")
    command = listen()

    if "hello" in command:
        talk("Hi there! How can I help you today?")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk("The current time is " + time)

    elif "search for" in command:
        query = command.replace("search for", "")
        talk("Searching for " + query)
        pywhatkit.search(query)

    elif "weather in" in command:
        city = command.replace("weather in", "").strip()
        weather_info = get_weather(city)
        talk(weather_info)

    elif "who is" in command:
        person = command.replace("who is", "").strip()
        info = wikipedia.summary(person, 2)
        talk(info)

    elif "remind me to" in command:
        task = command.replace("remind me to", "").strip()
        save_reminder(task)

    elif "send email" in command:
        talk("To whom should I send the email?")
        to_email = input("Enter receiver email: ")
        talk("What is the subject?")
        subject = input("Enter subject: ")
        talk("What should I say?")
        message = input("Enter message: ")
        send_email(to_email, subject, message)

    else:
        talk("Sorry, but i can't hear your voice..")

# Run the assistant
run_assistant()
