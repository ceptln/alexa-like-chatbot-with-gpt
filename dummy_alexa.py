import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import pyjokes
from gtts import gTTS
from playsound import playsound
import utils


def run_alexa():
    command = utils.take_command()
    print(command)
    if not command or 'thank you' in command:
        return True
    if 'play' in command:
        song = command.replace('play', '') 
        utils.talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        utils.talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command. replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        utils.talk(info)
    elif 'date' in command:
        utils.talk('sorry, I have a headache')
    elif 'are you single' in command:
        utils.talk('I am in a relationship with wifi')
    elif 'joke' in command:
        utils.talk(pyjokes.get_joke())
    else:
        utils.talk('please say the command again.')
    return False


if __name__ == '__main__':
    
    stop = False

    while not stop:
        stop = run_alexa()