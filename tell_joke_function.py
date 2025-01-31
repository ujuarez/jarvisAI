import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import smtplib
import os
import requests


def tell_joke():
    """Tell a random joke."""
    jokes = [
        "Why don’t programmers like nature? It has too many bugs!",
        "Why do Java developers wear glasses? Because they don’t see sharp!"
    ]
    speak(jokes[0])  # You can randomize this