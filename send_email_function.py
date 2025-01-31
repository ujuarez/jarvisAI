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


def send_email(to, content):
    """Send an email using stored credentials in `secrets.py`."""
    try:
        from secrets import EMAIL, PASSWORD  # Import credentials
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, to, content)
        server.close()
        speak("Email has been sent successfully!")
    except Exception as e:
        speak("Sorry, I was unable to send the email.")