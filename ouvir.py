#!/usr/bin/python
import io
import os
import json
from asterisk.agi import *
import speech_recognition as sr
import sys

agi = AGI()

idligacao = agi.get_variable('id')
#Funcao responsavel por ouvir e reconhecer a fala
def ouvir_microfone():
     #Habilita o microfone para ouvir o usuario
     r = sr.Recognizer()
     microfone = sr.AudioFile('/var/spool/asterisk/monitor/speech/'+str(idligacao)+'.wav')
     #Passa o audio para o reconhecedor de padroes do speech_recognition
     with microfone as source:
      audio = r.record(source)
      frase = r.recognize_google(audio,language='pt-BR')
     return frase
fala=ouvir_microfone()
agi.set_variable("OUTPUT",fala)
os.remove('/var/spool/asterisk/monitor/speech/'+str(idligacao)+'.wav')
