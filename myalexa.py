from distutils.cmd import Command
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say("  " + text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("\nlistening ...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'vikram' in command:
                command = command.replace('vikram', '')
                print(command)

    except:
        pass

    return command


var = True


def run_alexa():

    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what is' in command:
        x = command.replace('what is', '')
        info1 = wikipedia.summary(x, 1)
        print(info1)
        talk(info1)

    elif 'date' in command:
        talk('sorry, i have a headache')

    elif 'are you single' in command:
        talk('i am in a relationship with wifi')

    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())

    elif 'how are you' in command:
        talk('i am not fine, no thanks')
    elif 'turn off' in command:
        talk("ok byee")
        var = False
    elif 'love' in command:
        talk("sorry, i dont love you .i love only my owner")
    else:
        talk("  sorry i dont understand    come again ")


while var == True:

    run_alexa()
