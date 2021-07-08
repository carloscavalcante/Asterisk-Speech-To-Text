#!/usr/bin/python
import io
import os
import json
from asterisk.agi import *
import speech_recognition as sr
import sys

#chama a funcao AGI do Asterisk
agi = AGI()

#Traz o id que foi enviado para o asterisk no inicio da chamada.
idligacao = agi.get_variable('id')

#Funcao responsavel por ouvir e reconhecer a fala
def ouvir_microfone():
     r = sr.Recognizer()
     microfone = sr.AudioFile('/var/spool/asterisk/monitor/speech/'+str(idligacao)+'.wav')
     #Passa o audio para o reconhecedor de padroes do speech_recognition
     with microfone as source:
      audio = r.record(source)
      frase = r.recognize_google(audio,language='pt-BR')
     return frase
fala=ouvir_microfone()
#retorna a vaviavel do que foi falado para o Asterisk.
agi.set_variable("OUTPUT",fala)
#remove o arquivo.
os.remove('/var/spool/asterisk/monitor/speech/'+str(idligacao)+'.wav')
