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


def search_wikipedia(query):
    """Search Wikipedia and return summary."""
    try:
        speak("Searching Wikipedia...")
        results = wikipedia.summary(query, sentences=2)
        speak(f"According to Wikipedia, {results}")
    except wikipedia.exceptions.DisambiguationError as e:
        speak("Multiple results found. Please be more specific.")
    except wikipedia.exceptions.PageError:
        speak("No Wikipedia page found for this search.")