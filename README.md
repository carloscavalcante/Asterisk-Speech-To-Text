# Asterisk-Speech-To-Text

Instalar as dependencias:

yum install portaudio-devel alsa-lib-devel portaudio python python-pip python-devel libxslt-devel libffi-devel openssl-devel

pip install SpeechRecognition

pip install pyaudio

pip install pyst2

copie o arquivo ouvir.py para a pasta "/var/lib/asterisk/agi-bin"

Segue exemplo:

exten => 1234,1,Record(/var/spool/asterisk/monitor/speech/102030.wav,,5)

exten => 1234,n,Set(id=102030)

exten => 1234,n,AGI(ouvir.py,id)

exten => 1234,n,AGI(googletts.agi,${OUTPUT},pt-br)

exten => 1234,n,Hangup

