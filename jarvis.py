# import pyttsx3 #pip install pyttsx3 == it is used to convert text to speech
# import datetime
# import speech_recognition as sr
# import smtplib
# import pyaudio
# import wikipedia
# import webbrowser
# import os
# import requests

# from email.message import EmailMessage

# engine = pyttsx3.init()

# def speak(audio):
#     """Convert text to speech."""
#     engine.say(audio)
#     engine.runAndWait()



# def wish_me():
#     """Greet the user based on the time of day."""
#     hour = int(datetime.datetime.now().hour)
#     if hour < 12:
#         speak("Good morning!")
#     elif 12 <= hour < 18:
#         speak("Good afternoon!")
#     else:
#         speak("Good evening!")
#     speak("I am Jarvis. How can I assist you today?")



# def takeCommand():
#     """Listen to user command via microphone and convert to text."""
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         recognizer.pause_threshold = 1
#         audio = recognizer.listen(source)

#     try:
#         print("Recognizing...")
#         query = recognizer.recognize_google(audio, language='en-in')
#         print(f"User said: {query}")
#     except Exception as e:
#         print("Sorry, could not understand. Say that again please.")
#         return "None"
#     return query.lower()



# def time():
#     time = datetime.datetime.now().strftime("%I:%M:%S") # Hour = I, Min = M, Sec = S
#     speak(f"The current time is: {time}")



# def date():
#     # year = int(datetime.datetime.now().year)
#     # month = int(datetime.datetime.now().month)
#     # date = int(datetime.datetime.now().day)
#     # speak("the current date is: ")
#     # print(date)
#     # print(month)
#     # print(year)
#     date = datetime.datetime.now().strftime("%Y-%m-%d")
#     speak(f"Today's date is {date}")



# ######################################################################################
#     #######################################################################################

# def search_wikipedia(query):
#     """Search Wikipedia and return summary."""
#     try:
#         speak("Searching Wikipedia...")
#         results = wikipedia.summary(query, sentences=2)
#         speak(f"According to Wikipedia, {results}")
#     except wikipedia.exceptions.DisambiguationError as e:
#         speak("Multiple results found. Please be more specific.")
#     except wikipedia.exceptions.PageError:
#         speak("No Wikipedia page found for this search.")



# def open_website(site_name):
#     """Open a website in the browser."""
#     webbrowser.open(f"https://{site_name}.com")



# def send_email(to, content):
#     """Send an email using stored credentials in `secrets.py`."""
#     try:
#         from secrets import EMAIL, PASSWORD  # Import credentials
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.login(EMAIL, PASSWORD)
#         server.sendmail(EMAIL, to, content)
#         server.close()
#         speak("Email has been sent successfully!")
#     except Exception as e:
#         speak("Sorry, I was unable to send the email.")



# def get_weather():
#     """Fetch current weather details."""
#     API_KEY = "your_openweathermap_api_key"  # Replace with actual API Key
#     city = "Chicago"  # Change as needed
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

#     response = requests.get(url).json()
#     if response.get("main"):
#         temperature = response["main"]["temp"]
#         description = response["weather"][0]["description"]
#         speak(f"The temperature in {city} is {temperature}°C with {description}.")
#     else:
#         speak("Sorry, I couldn't fetch the weather details.")



# def take_screenshot():
#     """Take a screenshot and save it."""
#     screenshot_name = "screenshot.png"
#     os.system(f"scrot {screenshot_name}")  # Works on Linux. Use `pyautogui.screenshot()` for Windows.
#     speak("Screenshot taken successfully.")



# def tell_joke():
#     """Tell a random joke."""
#     jokes = [
#         "Why don’t programmers like nature? It has too many bugs!",
#         "Why do Java developers wear glasses? Because they don’t see sharp!"
#     ]
#     speak(jokes[0])  # You can randomize this

# ########################################################
# #####################################################################################   

# # def greeting():
# #     hour = datetime.datetime.now().hour
# #     if hour >= 6 and hour <12:
# #         speak("Good Morning Sir!")
# #     elif hour >= 12 and hour <18:
# #         speak("Good Afternoon Sir!")
# #     elif hour >= 18 and hour < 24:
# #         speak("Good Evening Sir!")
# #     else:
# #         speak("Good Night Sir!")

# ############################# 
#     ##############################

# if __name__ == "__main__":
#     wish_me()
#     while True:
#         command = takeCommand()

#         if "time" in command:
#             tell_time()
#         elif "date" in command:
#             tell_date()
#         elif "wikipedia" in command:
#             search_wikipedia(command.replace("wikipedia", ""))
#         elif "open youtube" in command:
#             open_website("youtube")
#         elif "open google" in command:
#             open_website("google")
#         elif "send email" in command:
#             speak("What should I say?")
#             content = takeCommand()
#             speak("Whom should I send it to?")
#             recipient = input("Enter recipient email: ")  # Input for demo purposes
#             send_email(recipient, content)
#         elif "weather" in command:
#             get_weather()
#         elif "joke" in command:
#             tell_joke()
#         elif "screenshot" in command:
#             take_screenshot()
#         elif "exit" in command:
#             speak("Goodbye!")
#             break
#         else:
#             speak("I'm not sure how to do that yet.")

# ##########################################
#             ##################################

# # if __name__ == "__main__":
# #     wishme()
# #     while True:
# #         query = take_command()

# #         if 'time' in query:
# #             time()

# #         elif 'date' in query:
# #             date()
        
# #         elif 'email' in query:
# #             try:
# #                 speak('what should i say?')
# #                 content = takeCommand()
# #                 sendEmail(content)
# #                 speak("email has been sent")
# #             except Exception as e:
# #                 print(e)
# #                 speak("u")



# # ######################
# #    # SEND EMAIL #

# # def sendEmail(receiver, subject, content):
# #     server = smtplib.SMTP('smpt.gmail.com', 587)
# #     server.starttls()
# #     server.login(senderemail, epwd)
# #     email = EmailMessage()
# #     email['From'] = senderemail
# #     email['To'] = receiver
# #     email['Subject'] = subject
# #     email.set_content(content)
# #     server.send_message(email)
# #     server.close()

# # sendEmail()

# # def takeCommandMIC():
# #     r = sr.Recognizer()
# #     with sr.Microphone as source:
# #         print("listening...")
# #         r.pause_threshold = 1
# #         audio = r.listen(source)
# #     try:
# #         print("Recoginziing...")
# #         query = r.recognize_google(audio, language="en-IN")
# #         print("User Said: "+query)
    
# #     except Exception as e:
# #         print(e)
# #         speak("Say that Again Please....")
# #         return "None"
    
# #     return query

# # while True:
# #     query = takeCommandMIC().lower()

# #     if 'time' in query:
# #         time()

# #     elif 'date' in query:
# #         date()

# #     elif 'email' in query:
# #         email_list = {
# #             'testemail':'email@gmail.com'
# #         }
# #         try:
# #             speak("To whom you want to send the mail?")
# #             name = takeCommandMIC()
# #             receiver = email_list[name]
# #             speak("what is the subject of the mail?")
# #             subject = takeCommandMIC()
# #             speak('what should i say?')
# #             content = takeCommandMIC()
# #             sendEmail(receiver, subject, content)
# #             speak("Email has been sent)")
# #         except Exception as e:
# #             print(e)
# #             speak("unable to end the email")
        
# #     elif 'offline' in query:
# #         quit()
    


############################################################
#####################################################################################



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