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



def tell_date():
    """Fetch current date."""
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    speak(f"Today's date is {date}")