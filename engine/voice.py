import datetime
import os
import smtplib
import webbrowser as wb
import urllib.request
import urllib.parse
import re

# google text to speech
# from gtts import gTTS
# pyttsx3
import pyttsx3
import speech_recognition as sr
import wikipedia
import sys

# print("Initializing Assistant...")
MASTER = "Samkit"

engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'english-us')
# engine.setProperty('rate', 100)
# Speak function will speak/Pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()

#This funtion will wish you as per the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    # print(hour)

    if hour>=0 and hour <12:
        print("good morning" + MASTER)

    elif hour>=12 and hour<18:
        print("good afternoon" + MASTER)

    else:
        print("good Evening" + MASTER)

    print("I am your assistant. How may I help you?")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kumaraman.rose@gmail.ocm', 'password')
    server.sendmail("harry@gmail.com", to, content)
    server.close()

#This function will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print("Listening...")
        audio = r.listen(source, phrase_time_limit=8)

    try :
        # print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        speak("Got it...")
        # print(query)
        print(f"you said: {query}\n")

    except Exception as e:
        print("Please try again...")
        query = None

    return query

#main program starting
def main():
    # speak("Initializing Assistant...")
    # wishMe()
    # print("starting...")
    query = takeCommand()
    query = query.lower()
    print(query)
    #Logic for executing tasks as per the query
    if 'open google' in query:
        #webbrowser.open('youtube.com')
        url = "https://www.google.com"
        # chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        # wb.get(chrome_path).open(url)
        wb.open(url)

    elif 'on google' in query:
        query = query.replace("on google", "")
        url = "https://www.google.com/search?q=" + query
        wb.open(url)

    elif 'wikipedia' in query:
        # speak('searching wikipedia...')
        # query = query.replace("wikipedia", "")
        # results = wikipedia.summary(query, sentences =2)
        # print(results)
        # speak(results)
        query = query.replace("wikipedia", "")
        print("https://en.wikipedia.org/wiki/" + "_".join(query.split()))
        # open this link in browser
        url = "https://en.wikipedia.org/wiki/" + "_".join(query.split())
        wb.open_new(url)

    elif 'open youtube' in query:
        #webbrowser.open('youtube.com')
        # url = "youtube.com"
        # chrome_path = 'c:/program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        # wb.get(chrome_path).open(url)
        wb.open_new("http://www.youtube.com")

    elif 'play' in query:
        query = query.replace("play", "")
        query_string = urllib.parse.urlencode({"search_query" : query})
        html_content = urllib.request.urlopen("https://www.youtube.com.hk/results?"+query_string)
        search_results = re.findall(r'url\"\:\"\/watch\?v\=(.*?(?=\"))', html_content.read().decode())
        if search_results:
            print("http://www.youtube.com/watch?v=" + search_results[0])
        wb.open_new("http://www.youtube.com/watch?v={}".format(search_results[0]))

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}")
        print(f"{MASTER} the time is {strTime}")

    elif 'open code' in query:
        codePath = "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

# while(True):
main()
sys.stdout.flush()