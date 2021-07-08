import speech_recognition as sr
#Funcao responsavel por ouvir e reconhecer a fala
def ouvir_microfone():
     #Habilita o microfone para ouvir o usuario
     r = sr.Recognizer()
     microfone = sr.AudioFile('/var/lib/asterisk/sounds/.wav')
     #Passa o audio para o reconhecedor de padroes do speech_recognition
     with microfone as source:
      audio = r.record(source)
      frase = r.recognize_google(audio,language='pt-BR')
      #Após alguns segundos, retorna a frase falada
      print("Você disse: " + frase)
     return frase
ouvir_microfone()
