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


def get_weather():
    """Fetch current weather details."""
    API_KEY = "your_openweathermap_api_key"  # Replace with actual API Key
    city = "Chicago"  # Change as needed
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url).json()
    if response.get("main"):
        temperature = response["main"]["temp"]
        description = response["weather"][0]["description"]
        speak(f"The temperature in {city} is {temperature}°C with {description}.")
    else:
        speak("Sorry, I couldn't fetch the weather details.")