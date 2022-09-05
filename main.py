from ast import parse
from datetime import datetime
import time
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia 
import pywhatkit



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
    
    print('Listening...')

    with sr.Microphone() as source:
        listener.pause_threshold = 1 #this is the pause time when you finish your command for ai to response
        #listener.adjust_for_ambient_noise(source, duration=1)
        #listener.dynamic_energy_threshold = True 
        
        input_command = listener.listen(source)
    
        try:
            print('Recognizing command...')
            query = listener.recognize_google(input_command, language='en_gb')
            print(f'Your command is: {query}')
        except Exception as err:
            #speak('Sorry, I did not get that, please say again')        
            print(err)
            query = 'please say again'
    
    return query

if __name__ == '__main__':
    speak('system checkup complete, initializing...')
    time.sleep(2)
    speak('greetings all')

    while True:
        query = parseCommand().lower().split()
        print(query)
        if 'sima' in query or 'cima' in query or 'cosima' in query:
            speak('What can I do for you master')
        #list commands
        if 'open' in query and 'youtube' in query or 'youtube' in query:
            webbrowser.open_new_tab('https://www.youtube.com')
            speak('youtube is open')
        if 'bye' in query or 'bye-bye' in query or 'cu' in query:
            speak('system shutting down, see you master')
            quit()
        if 'time' in query:
            time = datetime.now().strftime('%H:%M %p')
            print(time)
            speak('the current time is ' + time)
            
        
        

