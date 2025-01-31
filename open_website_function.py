import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import smtplib
import os
import requests


def open_website(site_name):
    """Open a website in the browser."""
    webbrowser.open(f"https://{site_name}.com")