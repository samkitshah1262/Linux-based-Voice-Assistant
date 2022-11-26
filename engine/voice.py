import datetime
import os
import smtplib
import webbrowser

import pyttsx3
import speech_recognition as sr
import wikipedia

print("Initializing Assistant")
MASTER = "Samkit"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
#Speak function will speak/Pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()

#This funtion will wish you as per the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    # print(hour)

    if hour>=0 and hour <12:
        speak("good morning" + MASTER)

    elif hour>=12 and hour<18:
        speak("good afternoon" + MASTER)

    else:
        speak("good Evening" + MASTER)

    speak("I am your assistant. How may I help you?")

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
        #webbrowser.open('youtube.com')
        print(1)
        url = "google.com"
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        webbrowser.get(chrome_path).open(url)

    elif 'wikipedia' in query.lower():
        speak('searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences =2)
        print(results)
        speak(results)

    elif 'open youtube' in query.lower():
        #webbrowser.open('youtube.com')
        url = "youtube.com"
        chrome_path = 'c:/program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'play music' in query.lower():
        songs_dir = "C:\\Users\\Dell\\Desktop\\Photos\\audio"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}")

    elif 'open code' in query.lower():
        codePath = "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
    
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
        os.system('start cmd')
        # os.system("start /wait cmd /c {command}")
    elif 'open notepad' in query.lower():
        os.system('start notepad')    
    elif 'open calculator' in query.lower():
        os.system('start calc')
    elif 'open paint' in query.lower():
        os.system('start mspaint')
    elif 'open camera' in query.lower():
        os.system('start microsoft.windows.camera:')
    elif 'open control panel' in query.lower():
        os.system('start control')
    elif 'open file explorer' in query.lower():
        os.system('start explorer')
    elif 'open task manager' in query.lower():
        os.system('start taskmgr')
    elif 'open windows media player' in query.lower():
        os.system('start wmplayer')
    elif 'open windows store' in query.lower():
        os.system('start ms-windows-store:')
    elif 'shutdown' in query.lower():
        os.system('shutdown /s /t 1')
main()