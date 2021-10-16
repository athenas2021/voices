import speech_recognition as sr

def ouvir():
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Diga algo: ")
        audio = microfone.listen(source)
    try:
        frase = microfone.recognize_google(audio,language='pt-BR')
        print(frase)
    except:
        print('Não entendi')
    return frase

ouvir()
