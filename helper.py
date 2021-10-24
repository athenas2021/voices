import speech_recognition as sr
import pyttsx3
import os
import wikipedia
from re import search       

navegador = ["navegador", "chrome", "crome", "opera","internet"]
# Função para ouvir (retorna frase em texto)
def ouvir():
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        audio = microfone.listen(source)
    try:
        frase = (microfone.recognize_google(audio,language='pt-BR')).lower()
        print(frase)
    except:
        print('Não entendi')
    return frase

# Função para falar (recebe texto)
def falar(texto):
    engine = pyttsx3.init()

    #voices = engine.getProperty('voices')
   # for voice in voices:
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_ptBR_DanielM')
     #3  print( voice.id)
       
       #engine.say('The quick brown fox jumped over the lazy dog.')

    engine.say(texto)
    engine.runAndWait() 

def mudar_locutor(locutor):
    # Maria 0
    # Daniel 2
    print()
    # engine = pyttsx3.init()
    # voices = engine.getProperty('voices')
    # for voice in voices:
    #    engine.setProperty('voice', voice.id)
    #    engine.say('The quick brown fox jumped over the lazy dog.')
    # engine.runAndWait()


falar('Olá bom dia, o que  gostaria?')
frase1 = ouvir()
falar('Você falou:') 
falar(frase1)


if search('chrome', frase1):
    falar('Ok, estou abrindo o Google Chrome para você')
    os.system("start Chrome.exe")
if search('wikipédia', frase1):
    falar('O que você gostaria de pesquisar?')
    frasex = ouvir()
    falar('pesquisando: ')
    falar(frasex)
    falar(wikipedia.summary(frasex, sentences=2))  
#falar('Deseja abrir navegador Google Chrome?')
#os.system("start Chrome.exe")  
#falar(wikipedia.search("Bill"))    




