#!/usr/bin/python
import io
import os
import json
from asterisk.agi import *
import speech_recognition as sr
import sys
from unidecode import unidecode

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
try:
     fala=ouvir_microfone()
except:
     fala=''
#retirar os acentos do que a pessoa falou
fala=unidecode(fala.upper())


agi.set_variable("FALA",fala.upper())
if(len(fala)>=2 and len(fala)<=8):
     fala='S'
else:
     fala='N'
agi.set_variable("OUTPUT",fala)
os.remove('/var/spool/asterisk/monitor/speech/'+str(idligacao)+'.wav')