import datetime
import os
import smtplib
import webbrowser

# google text to speech
from gtts import gTTS
import speech_recognition as sr
import wikipedia
import sys

print("Initializing Assistant")
MASTER = "Samkit"

# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)
#Speak function will speak/Pronounce the string which is passed to it
# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

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
        print("Listening...")
        audio = r.listen(source, phrase_time_limit=10)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        # print(query)
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        query = None

    return query

#main program starting
def main():
    # speak("Initializing Assistant...")
    # wishMe()
    # print("starting...")
    query = takeCommand()
    print(query.lower())
    # #Logic for executing tasks as per the query
    # if 'open google' in query.lower():
    #     #webbrowser.open('youtube.com')
    #     print(1)
    #     url = "google.com"
    #     chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    #     webbrowser.get(chrome_path).open(url)

    # elif 'wikipedia' in query.lower():
    #     speak('searching wikipedia...')
    #     query = query.replace("wikipedia", "")
    #     results = wikipedia.summary(query, sentences =2)
    #     print(results)
    #     speak(results)

    # elif 'open youtube' in query.lower():
    #     #webbrowser.open('youtube.com')
    #     url = "youtube.com"
    #     chrome_path = 'c:/program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    #     webbrowser.get(chrome_path).open(url)

    # elif 'play music' in query.lower():
    #     songs_dir = "C:\\Users\\Dell\\Desktop\\Photos\\audio"
    #     songs = os.listdir(songs_dir)
    #     print(songs)
    #     os.startfile(os.path.join(songs_dir, songs[0]))

    # elif 'the time' in query.lower():
    #     strTime = datetime.datetime.now().strftime("%H:%M:%S")
    #     speak(f"{MASTER} the time is {strTime}")

    # elif 'open code' in query.lower():
    #     codePath = "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    #     os.startfile(codePath)
    
    # elif 'email to raj' in query.lower():
    #     try:
    #         speak("what should i send")
    #         content = takeCommand()
    #         to = "harry@gmail.ocm"
    #         sendEmail(to, content)
    #         speak("Email has been sent to raj")
    #     except Exception as e:
    #         print(e)



main()
sys.stdout.flush()