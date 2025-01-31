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

def tell_time():
    """Fetch current time."""
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The time is {time}")