import speech_recognition as sr
import pyttsx3
import os

navegador = ["navegador", "chrome", "crome", "opera","internet"]
# Função para ouvir (retorna frase em texto)
def ouvir():
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        falar('teste')
        print("Diga algo: ")
        audio = microfone.listen(source)
    try:
        frase = (microfone.recognize_google(audio,language='pt-BR')).lower()
        print(frase)
        if "navegador" or "Chrome" or "chrome" or "crome" or "Crome" in frase:
            print()
            #os.system("start Chrome.exe")
    except:
        print('Não entendi')
    return frase

# Função para falar (recebe texto)
def falar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait() 

def mudar_locutor(locutor):
    # Maria 0
    # Daniel 2
    print()
ouvir()


