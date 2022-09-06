from ast import parse
from datetime import datetime
from logging import shutdown
import time
import speech_recognition as sr
import pyttsx3
import wikipedia 
import pywhatkit
import subprocess


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'english+f5')
activation_words = ['sima', 'cima', 'cosima', 'zima', 'seamart', 'isomer', 'shimmer', 'seam', 'simmer', 'seema']
shutdown_words = ['bye','cu', 'Cu', 'bye-bye', 'goodbye']
compliment_words = ['good job','very good', 'nice work', 'well done', 'very well']

def speak(text, rate = 178):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def parseCommand():
    listener = sr.Recognizer()
    listener.energy_threshold = 4000
    listener.dynamic_energy_threshold = True 
    
    print('Listening...')

    with sr.Microphone() as source:
        listener.pause_threshold = 0.5 #this is the pause time when you finish your command for ai to response
        listener.adjust_for_ambient_noise(source, duration=0.5)
        input_command = listener.listen(source)
    
    try:
        print('Recognizing command...')
        query = listener.recognize_google(input_command, language='en_gb')
        print(f'Your command is: {query}')
    except Exception as err:   
        query = ''
    
    return query

if __name__ == '__main__':
    speak('system checkup complete, initializing...')
    time.sleep(2)
    while True:
        speak('please state passcode')
        query = parseCommand().lower().split()
        for word in query:
            if word in activation_words:
                speak('Greetings What can I do for you master')
   
                while True:
                    query = parseCommand().lower().split()
                    query_str = ' '.join(query)
                    for word in query:
                        if word in activation_words:
                            speak('yes master')
                    if 'open youtube' in query_str or 'turn on youtube' in query_str:
                        youtube = subprocess.Popen(['firefox', 'https://www.youtube.com'])
                        speak('youtube is open')
                    if 'close youtube' in query_str or 'turn off youtube' in query_str:
                        try:
                            youtube.kill()
                            speak('youtube turned off')
                        except Exception as err:
                            speak('I can\'t close it master, something went wrong')
                    for word in query:
                        if word in shutdown_words or 'shut down' in query_str:
                            speak('system shutting down, see you master')
                            quit()
                    if 'time' in query:
                        time = datetime.now().strftime('%H:%M %p')
                        print(time)
                        speak('the current time is ' + time)
                    if 'play' in query:
                        speak(query_str)
                        pywhatkit.playonyt(' '.join(query[1:])) 
                    for word in compliment_words:
                        if word in query_str:
                            speak('thank you master')
                    if 'thank you' in query_str:
                        speak('you are welcome master')
        else:
            speak('incorrect passcode')
        
        

