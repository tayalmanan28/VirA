import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import time

engine = pyttsx3.init('espeak')
engine.setProperty('rate',130)
#voices = engine.getProperty('voices')
engine.setProperty('voice', 'mb-en1')


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('listening...')
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            command= r.recognize_google(audio)
    except:
        command = 'ncomm'
    return command


def run_VirA():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'what is' in command:
        try:
          subject = command.replace('what is', '')
          info = wikipedia.summary(subject, 1)
          print(info)
          talk(info)
        except:
          talk('Sorry Sir, can you repeat it again')
    elif 'who is' in command:
        try:
          subject = command.replace('who is', '')
          info = wikipedia.summary(subject, 1)
          print(info)
          talk(info)
        except:
          talk('Sorry Sir, can you repeat it again')
    elif 'Palace' in command:
        talk('playing Palace Theme')
        pywhatkit.playonyt('Palace Theme Rathore Kishore')
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'wait' in command:
        print('Okay Sir, I will wait')
        import time
        time.sleep(60)
    elif 'ncomm' in command:
        print('Waiting for Next Command')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Sir, can you please say the command again?')


while True:
    run_VirA()
