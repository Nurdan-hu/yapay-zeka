import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os
from nltk.tokenize import sent_tokenize, word_tokenize

def kelime_sayisi_hesapla(metin):
    kelimeler = metin.split()
    return len(kelimeler)


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
    print(voice)
    metin= voice
    kelimeler = word_tokenize(metin)
    kelimeler.split()
    kelime_sayisi = len(kelimeler)
    print(f"Kelime sayısı: {kelime_sayisi}")
    exit()

def speak(string):
    tts = gTTS(string, lang='tr')
    rand = random.randint(1,10000)
    file = 'audio-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)
