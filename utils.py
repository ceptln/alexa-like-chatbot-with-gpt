import datetime
import openai
import speech_recognition as sr
import datetime
from gtts import gTTS
from playsound import playsound

listener = sr.Recognizer()
language='en'

def open_file(filepath:str)-> str:
    '''This function reads a file'''
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


def talk(text: str)-> None:
    '''This function converts a string to an mp3 file and plays it'''
    time = datetime.datetime.now().strftime('%Y%m%d%s')
    audio = gTTS(text=text, lang=language, slow=False)    
    audio_path = f"audios/audio_{time}.mp3"
    audio.save(audio_path)
    playsound(audio_path)


def take_command():
    '''This function activates the microphone, records an audio message and converts it to text'''
    try:
        with sr.Microphone() as source:
            print('listening ...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
        return command
    except:
        print("Recording didn't work")


def gpt3_completion(prompt, engine='text-davinci-003', temp=0, 
                    top_p=1.0, tokens=300, freq_pen=0.0, pres_pen=0.0, 
                    ):
    prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temp,
        max_tokens=tokens,
        top_p=top_p,
        frequency_penalty=freq_pen,
        presence_penalty=pres_pen)
    text = response['choices'][0]['text'].strip()
    return text