import schedule
import pygame

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
schedule.every(35).minutes.do(drink_water_notification)
schedule.every(60).minutes.do(exercise_notification)
schedule.every(90).minutes.do(eye_exercise_notification)

# Run the notifications
while True:
    schedule.run_pending()
    
# Quit the script
quit()
