### Project: **JarvisAI - Voice Assistant**

#### 1. **Install Dependencies** (Run in Terminal)

# pip install pyttsx3 SpeechRecognition wikipedia requests datetime smtplib
#pip install pyaudio



### **1. `jarvis.py` - Main Program**
# This file contains all the core functionalities.


import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import smtplib
import os
import requests


from speak_function import speak
from wish_me_function import wish_me
from take_command_function import take_command
from tell_time_function import tell_time
from tell_date_function import tell_date
from search_wikipedia_function import search_wikipedia
from open_website_function import open_website
from send_email_function import send_email
from get_weather_function import get_weather
from take_screenshot_function import take_screenshot
from tell_joke_function import tell_joke

(wish_me)


(take_command)


(tell_time)


(tell_date)


(search_wikipedia)


(open_website)


(send_email)


(get_weather)


(take_screenshot)


(tell_joke)


# Main Execution
if __name__ == "__main__":
    wish_me()
    while True:
        command = take_command()

        if "time" in command:
            tell_time()
        elif "date" in command:
            tell_date()
        elif "wikipedia" in command:
            search_wikipedia(command.replace("wikipedia", ""))
        elif "open youtube" in command:
            open_website("youtube")
        elif "open google" in command:
            open_website("google")
        elif "send email" in command:
            speak("What should I say?")
            content = take_command()
            speak("Whom should I send it to?")
            recipient = input("Enter recipient email: ")  # Input for demo purposes
            send_email(recipient, content)
        elif "weather" in command:
            get_weather()
        elif "joke" in command:
            tell_joke()
        elif "screenshot" in command:
            take_screenshot()
        elif "exit" in command:
            speak("Goodbye!")
            break
        else:
            speak("I'm not sure how to do that yet.")