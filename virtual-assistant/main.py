import pyttsx3
import webbrowser
import smtplib
import random 
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import json
import requests
import emoji
from datetime import datetime


engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('Your_App_ID')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Erayus: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int (datetime.now().hour)
    if currentH >= 0 and currentH < 12:   
        speak('Good Morning Aiden!')
        print(emoji.emojize(":grinning_face_with_big_eyes:"))

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon Aiden!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening Aiden!')

greetMe()

speak('Hello Aiden, I am your digital assistant Erayus the Lady Erayus')
speak('How may I help you Aiden')


def myCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Sorry Aiden! I didnt get that! Try typing the command!')
        query = str(input('Command: '))

    return query

def getWeatherJSONData():
    res = requests.get('https://api.ipify.org')
    ip = res.text
    send_url = ''


