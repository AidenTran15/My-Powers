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

client = wolframalpha.Client('Your_App_ID'

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Erayus: '= audio)
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
    send_url = 'http://api.ipstack.com/'+ip+'?access_key=7e5ea1fda803cb076716badc347f0885&output=json&legacy=1'
    r = requests.get(send_url)
    j = json.loads(r.text)
    lat = j['latitude']
    lon = j['longtitude']
    response = requests.get('https://api.darksky.net/forecast/24cd61bddf35c80d5e2ff15663b50ec8/'+str(lat)+','+str(lon)+'')
    jsonWeather = json.loads(response.text)
    return jsonWeather


    if __name__ == '__main__':

        while True:

            query = myCommand()
            query = query.lower()

            if "open youtube" in query:
                speak('yes sir')
                




