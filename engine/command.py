import time
import pyttsx3
import speech_recognition as sr
import eel

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',174)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()

def takecommand():

    listener = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening...')
        eel.DisplayMessage('Listening...')
        listener.pause_threshold = 1
        listener.adjust_for_ambient_noise(source)

        audio = listener.listen(source,10,6)
    
    try:
        print('Recognizing...')
        eel.DisplayMessage('Recognizing...')
        query = listener.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        time.sleep(3)

    except:
        print("sorry could not recognise")      
    return query.lower()

@eel.expose
def allCommands():
    try:
        query = takecommand()
        print(query)

        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
        elif "play" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)
        else:
            print('not run')
    except:
        print('error')

    eel.ShowHood()



