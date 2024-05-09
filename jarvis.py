import ctypes
from datetime import datetime
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib
import pyjokes
import ecapture
import subprocess
import numpy as np


engine =pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
#print(voices[1].id)

engine.setProperty('voice',voices[1].id)

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('clayt3947@gmail.com','91137872hsg')
    server.sendmail('clayt3947@gmail.com',to,content)
    server.close()
    

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int (datetime.datetime.now().hour)
    if hour>=0 and hour <= 12:
        speak("Good Morning sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir") 
    else:
        speak("good evening sir")
    speak("I am Friday , how can i help you")    
    
    
def takeCommand():
    #it take input from microphone  and returns string output
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        
        r.pause_threshold=1
        audio=r.listen(source)
         
        
    try:
        print("Recognizing.....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said :{query}\n")
      
    except Exception as e:
        #print e
        
        print("say that again please....")
        return "None"
    return query
                
                
        
if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        # speak(query)
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("searching in wikipedia.....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
            
        
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")    
            
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
            
        elif 'play music' in query:
            music_dir="D:\\music"
            songs=os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir,songs[random.randint(0,6)]))
            
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"sir ,the time is {strTime}")
            
        elif 'open vs code' in query:
            codePath = "C:\\Users\\Himanshu Singh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(codePath)
            
        elif 'send email' in query:
            try:
                speak("what should i say ?")
                content=takeCommand()
                to="hsgbxrssm@gmail.com"
                sendEmail(to,content)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry something went wrong")
                
        elif 'open whatsapp' in query:
            
            webbrowser.open("whatsapp.com")   
                
       
        elif 'friday rest' in query:
            speak("ok sir")
            os._exit(0)
            
        elif 'joke' in query:
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())
            
        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
                
        elif 'today cricket score' in query:
            webbrowser.open("cricbuzz.com")
            
        elif 'open college website' in query:
            webbrowser.open("https://iiitn.ac.in")
        
  