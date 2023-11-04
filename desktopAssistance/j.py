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


take_command()
while True:
    query=take_command().lower()
    if "wake up" in query:
        speak(" How can I help you? ")
    while True:
        query = take_command()
        if query is not None:
            query = query.lower()

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
            elif 'chatgpt' or 'chat GPT' or 'chat'  in query:
                webbrowser.open('https://chat.openai.com/')
                speak("Opening ChatGPT...")
            elif 'open bard' or 'open board' or 'open bod'or 'Board' or 'Bard' in query:
                webbrowser.open('https://bard.google.com/')
                speak("Opening Bard...")
            elif 'open Visual studio code' in query:
                path="C:\\Users\\Eneeya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(path)
            elif 'the time' in query:
                time=datetime.datetime.now().strftime("%H:%M")
                speak(time)
            elif 'quit' or 'Quit' or 'exit' or 'Exit' in query:
                speak("quitting")
                break
            elif 'exit' in query:
                exit()
        except wikipedia.exceptions.PageError:
            print("Could not find the page on Wikipedia.")
            print("Please try searching for a different topic or using different keywords.")

# Initialize pygame mixer
pygame.mixer.init()

# Define the notification functions
def play_audio(audio_file):
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

def drink_water_notification():
    print("Time to drink water!")
    play_audio("water.mp3")

def exercise_notification():
    print("Time to have a walk!")
    play_audio("exercise.mp3")

def eye_exercise_notification():
    print("Time to do an eye exercise!")
    play_audio("eye_exercise.mp3")

# Schedule the notifications
schedule.every(10).seconds.do(drink_water_notification)
schedule.every(60).minutes.do(exercise_notification)
schedule.every(25).minutes.do(eye_exercise_notification)

# Run the notifications
while True:
    schedule.run_pending()
    
# Quit the script
quit()
