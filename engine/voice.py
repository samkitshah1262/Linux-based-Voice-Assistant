import datetime
import os
import smtplib
import webbrowser as wb
import urllib.request
import urllib.parse
import re
import time
# google text to speech
# from gtts import gTTS
# pyttsx3
import pyttsx3
import speech_recognition as sr
import wikipedia
import sys
import subprocess

#read a javascript file using python
def readjs():
    f=open("..\GUI\output.txt","r")
    x=f.read()
    print(f.read())
    if(x=="1"):
        sys.exit()
    return

# # print("Initializing Assistant...")
MASTER = "Samkit"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'english-us')

def hi():
    # speak("Initializing Assistant...")
    wishMe()

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
        speak("Good Morning" + MASTER)
        print("Good morning " + MASTER)

    elif hour>=12 and hour<18:
        speak("Good Afternoon" + MASTER)
        print("Good afternoon " + MASTER)

    else:
        speak("Good Evening" + MASTER)
        print("Good Evening " + MASTER)

    # speak("I am Beetee. Please tell me how may I help you")
    print("I am BeeTee. How may I help you?")

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
        print("Listening...")
        audio = r.listen(source, phrase_time_limit=8)
    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        speak("Got it...")
        print(query)
        print(f"you said: {query}\n")

    except Exception as e:
        print("Please try again...")
        query = None

    return query

#main program starting
def main():
    # wishMe()
    # print("starting...")
    query = takeCommand()
    if(query==None):
        speak('No command given , Try again in some time')
        return
    query = query.lower()
    speak(query)
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
        os.system("code")
        speak("Done")
    
    elif 'email to raj' in query.lower():
        try:
            speak("what should i send")
            content = takeCommand()
            to = "harry@gmail.ocm"
            sendEmail(to, content)
            speak("Email has been sent to raj")
        except Exception as e:
            print(e)
    elif 'open terminal' in query.lower():
        os.system("gnome-terminal")
        speak("Done")
    elif 'open notepad' in query.lower():
        os.system("gedit")
        speak("Done")
    elif 'open calculator' in query.lower():
        os.system("gnome-calculator")
        speak("Done")
    elif 'open camera' in query.lower():
        os.system('cheese')
        speak("Done")
    elif 'open file explorer' in query.lower():
        os.system('nautilus')
        speak("Done")
    elif 'open task manager' in query.lower():
        os.system('gnome-system-monitor')
        # speak("opening task manager")
        os.system('start taskmgr')
        speak("Done")
    elif 'shutdown' in query.lower():
        speak("shutting down")
        os.system('shutdown now')
    elif 'screenshot' in query.lower():
        # speak("taking screenshot")
        os.system('gnome-screenshot')
        speak("Done")
def lessgo():
    hi()
    main()
    while True:
        readjs()
        # speak("Ready again 1")
        query=takeCommand()
        if query==None:
            time.sleep(3)
            continue
        elif(query.lower()=='wake up'):
            # speak(f"Hello {MASTER} , How can i help you")
            main()
        # elif(query.lower()=='sleep'):
        elif(query.lower()=="exit"):
            speak("Exiting")
            break
        
        # speak("Do you want to continue")
        # speak("Ready again 2")
        # samkit=10



lessgo()
sys.stdout.flush()