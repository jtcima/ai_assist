from datetime import datetime
import time
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia 



engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'english+f5')
activationword = 'cima'

def speak(text, rate = 178):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def parseCommand():
    listener = sr.Recognizer()
    listener.energy_threshold = 4000
    print('Listening...')

    with sr.Microphone() as source:
        listener.pause_threshold = 2
        input_command = listener.listen(source)
    
    try:
        print('Recognizing command...')
        query = listener.recognize_google(input_command, language='en_gb')
        
        print(f'Your command is: {query}')
        speak(f'Your command is {query}')
    except Exception as err:
        print('Sorry, the command is unclear, please say again')
        speak('Sorry, I did not get that, please say again')        
        print(err)
        return None
    return query

if __name__ == '__main__':
    speak('system checkup complete, initialzing...')
    time.sleep(2)
    speak('greetings')

    while True:
        query = parseCommand().lower().split()

        #list commands

