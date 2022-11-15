import datetime
import os
import smtplib
import webbrowser
import random
import pyttsx3
import speech_recognition as sr
import wikipedia
import pyjokes
import requests

print("Initializing Assistant")
MASTER = "Samkit"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
#Speak function will speak/Pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()
    # rate = engine.getProperty('rate')   # getting details of current speaking rate
    # print (rate)                        #printing current voice rate
    # engine.setProperty('rate', 125)     # setting up new voice rate


#This funtion will wish you as per the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    # print(hour)
    if hour>=0 and hour <12:
        speak("good morning" + MASTER)
    elif hour>=12 and hour<18:
        speak("good afternoon" + MASTER)
    else:
        speak("good evening" + MASTER)
    speak("I am your assistant. How may I help you?")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('xvyxutsjst@gmail.com', '#xvyxutsjst_1')
    server.sendmail("xvyxutsjst@gmail.com", to, content)
    server.close()

#This function will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        speak(query)
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        query = None

    return query

#main program starting
def main():
    speak("Initializing Assistant...")
    # wishMe()
    query = takeCommand()
    print(query.lower())
    #Logic for executing tasks as per the query
    if 'open google' in query.lower():
        url = "google.com"
        edge_path = 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
        os.startfile(edge_path)
        webbrowser.open(url)
    elif 'google' in query.lower():
        query = query.replace("google", "")
        url = "google.com/search?q=" + query.lower()
        edge_path = 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
        os.startfile(edge_path)
        webbrowser.open(url)
    elif 'on youtube' in query.lower():
        query = query.replace("on youtube", "")
        # 
        query = query.replace(" ", "+")
        url = "https://www.youtube.com/results?search_query=" + query.lower()
        edge_path = 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
        os.startfile(edge_path)
        webbrowser.open(url)
    elif 'wikipedia' in query.lower():
        speak('searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences =2)
        print(results)
        speak(results)
    elif 'play' in query.lower():
        query = query.replace("play", "")        
        url = "https://www.youtube.com/results?search_query=" + query.lower()
        edge_path = 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
        os.startfile(edge_path)
        webbrowser.open(url)
    # tell me a joke functionality using jokes library
    elif 'tell me a joke' in query.lower():
        joke = pyjokes.get_joke(category=random.choice(['neutral', 'all','chuck','twister']))
        print(joke)
        speak(joke)
    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}")
    elif 'open code' in query.lower():
        print(2)
        codePath = "C:\\Program Files\Microsoft VS Code\Code.exe"
        os.startfile(codePath)
    elif 'with code' in query.lower():
        print(3)
        codePath = "F:\data"

    elif 'roast me' in query.lower():
        # request to api
        url = "https://evilinsult.com/generate_insult.php?lang=en"
        response = requests.get(url)
        print(response.text)
        speak(response.text)
        
    elif 'email to' in query.lower():
        try:
            speak("what should i send")
            content = takeCommand()
            # to = "harry@gmail.ocm"
            speak("Who should i send it to")
            to = takeCommand()
            sendEmail(to, content)
            speak("Email has been sent to " + to)
        except Exception as e:
            print(e)

main()