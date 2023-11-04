import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import os
import sys
import schedule
import pygame

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning! ")
    elif hour >=12 and hour < 16:
        speak(" good afternoon! ")
    else:
        speak(" Good evening! ")

wish_me()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(" Listening ")
        r.pause_threshold = 1
        audio=r.listen(source)
  
    try:
        print(" please wait for a few minutes ")
        query = r.recognize_google(audio, language='en-in')
        print("you said", query)
        return query 
    except Exception as e:
#        print(e)
        print(" Could you please repeat ? ")
#        query = none
        return "error"



while True:
    query = take_command().lower()  # Get user input and convert to lowercase
    if "wake up" in query:
        speak("How can I help you?")
    else:
        try:
            if 'wikipedia' in query:
                speak("Searching in Wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=1)
                print("According to Wikipedia:")
                print(results)
                speak("According to Wikipedia:")
                speak(results)
            elif "youtube" in query:
                webbrowser.open('https://www.youtube.com/')
                speak("Opening YouTube...")
            elif 'chatgpt' in query or 'chat GPT' in query or 'chat' in query:
                webbrowser.open('https://chat.openai.com/')
                speak("Opening ChatGPT...")
            elif 'open bard' in query or 'open board' in query or 'open bod' in query or 'Board' in query or 'Bard' in query:
                webbrowser.open('https://bard.google.com/')
                speak("Opening Bard...")
            elif 'open Visual studio code' in query or 'code'.lower() in query:
                path = "C:\\Users\\Eneeya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(path)
            elif 'the time' in query:
                time = datetime.datetime.now().strftime("%H:%M")
                speak(time)
            elif 'quit' in query or 'exit' in query:
                speak("Quitting")
                break  # Exit the loop
        except wikipedia.exceptions.PageError:
            print("Could not find the page on Wikipedia.")
            print("Please try searching for a different topic or using different keywords.")

# ...

# Remove the following lines, as they are not needed
# Initialize pygame mixer
# Define the notification functions
# Schedule the notifications
# Run the notifications
# Quit the script
