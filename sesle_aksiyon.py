import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os
import turtle as t

r = sr.Recognizer()

def record(ask = False):
    with sr.Microphone() as source:
            if ask:
                speak (ask)
            audio = r.listen(source)
            voice = ''
            try:
                voice = r.recognize_google (audio , language ='tr-TR')
            except sr.UnknownValueError:
                speak ('anlayamadım')
            except sr.RequestError:
                speak('sistem çalışmıyor')
            return voice
def response(voice):
    if 'kare çiz' in voice:
        for a in range (4):
            t.speed(10)
            t.forward(100)
            t.right(90)
    if 'yuvarlak çiz' in voice:
        r = 50
        t.circle(r) 
def speak(string):
    tts = gTTS(string, lang='tr')
    rand = random.randint(1,10000)
    file = 'audio-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)

speak('nasıl yardımcı olabilirim?')
time.sleep(1)
while 1:
    voice = record()
    print(voice)
    response(voice)
