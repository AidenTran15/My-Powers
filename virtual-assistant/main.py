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
# import emoji
from datetime import datetime


engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('Your_App_ID')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)
name =''

def speak(audio):
    print('Erayus: ' + audio)
    engine.say(audio)
    engine.runAndWait()

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
        speak('Sorry '+ name+ '! I didnt get that! Try typing the command!')
        query = str(input('Command: '))

    return query

def greetMe():
    speak('Hello there, may I ask for your name first?');
    name = myCommand()
    name = name.title()
    currentH = int (datetime.now().hour)
    if currentH >= 0 and currentH < 12:   
        speak('Good Morning, '+ name + "!")

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon, '+ name + "!")

    if currentH >= 18 and currentH !=0:
        speak('Good Evening, ' + name + "!")
    speak('Hello ' + name + ', I am your digital assistant Erayus the Lady Erayus')
    speak('How may I help you '+ name + '?')

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
            webbrowser.open('www.youtube.com')

        elif "open google" in query:
            speak("yes sir")
            webbrowser.open('https://www.google.com.au/')

        elif "open gmail" in query:
            speak("yes sir")
            webbrowser.open('www.gmail.com')

        elif "open instagram" in query:
            speak("yes sir")
            webbrowser.open('www.instagram.com')
            
        elif "open facebook" in query:
            speak('yes sir')
            webbrowser.open('www.facebook.com')
            
        elif "open messenger" in query:
            speak("yes sir")
            webbrowser.open('www.facebook.com')
            
        elif "open hanout" in query:
            speak('yes sir')
            webbrowser.open('www.hangout.com')

        elif "movie" in query:
            speak('yes sir')
            webbrowser.open('http://topphimhd.com/tag/banhtv/')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak(' Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", "Your_Password")
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Aiden! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('yes sir')
            speak('Bye Aiden, have a good day.')
            sys.exit()
            



    




                



greetMe()

