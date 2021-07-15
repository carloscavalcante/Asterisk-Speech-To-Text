# Asterisk-Speech-To-Text

Este recurso é utilizado para reconhecimento de voz pelo Asterisk / Issabel, possibilitando inúmeras funções de acordo com a resposta.


Instalar as dependencias:

yum install portaudio-devel alsa-lib-devel portaudio python python-pip python-devel libxslt-devel libffi-devel openssl-devel

pip install SpeechRecognition

pip install pyaudio

pip install unidecode

pip install pyst2

copie o arquivo ouvir.py para a pasta "/var/lib/asterisk/agi-bin"

crie uma pasta dentro de monitor chamada "speech" ou como desejar.

Segue exemplo:

exten => 1234,n,Set(id=102030)

exten => 1234,1,Record(/var/spool/asterisk/monitor/speech/${id}.wav,,5)

exten => 1234,n,AGI(ouvir.py,id)

exten => 1234,n,NoOp(${OUTPUT})

exten => 1234,n,Hangup

