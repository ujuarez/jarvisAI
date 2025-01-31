import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import smtplib
import os
import requests


# Initialize Text-to-Speech Engine
engine = pyttsx3.init()

def speak(audio):
    """Convert text to speech."""
    engine.say(audio)
    engine.runAndWait()