import pyttsx3
import speech_recognition as sr
import datetime 

engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') 

engine.setProperty('voice', voices[1].id)


def speak(audio):
   engine.say(audio) 
   engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("good afternoon!")
    else:
        speak("Good evening!")
    
    speak("Sir,I am Lucy. Please tell me how may i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n" )

    except Exception as e:
        print("Say that again please...")
        return "None"

    return query

if __name__=="__main__" :
    wishMe()
    while True:
        query = takeCommand().lower()
     
