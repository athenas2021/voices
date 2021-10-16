import pyttsx3

"""  Saving voice to a file """
# engine = pyttsx3.init()
# engine.save_to_file('Hello World' , 'test.mp3')
# engine.runAndWait()

"""  Listening for events """
# def onStart(name):
#    print 'starting', name
# def onWord(name, location, length):
#    print 'word', name, location, length
# def onEnd(name, completed):
#    print 'finishing', name, completed
# engine = pyttsx3.init()
# engine.connect('started-utterance', onStart)
# engine.connect('started-word', onWord)
# engine.connect('finished-utterance', onEnd)
# engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()

""" Changing voices """
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# for voice in voices:
#    engine.setProperty('voice', voice.id)
#    engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()


""" Changing speech rate """
# engine = pyttsx3.init()
# rate = engine.getProperty('rate')
# engine.setProperty('rate', rate+50)
# engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()

""" Changing volume """
# engine = pyttsx3.init()
# volume = engine.getProperty('volume')
# engine.setProperty('volume', volume-0.25)
# engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()


""" Running a driver event loop """
# engine = pyttsx3.init()
# def onStart(name):
#    print 'starting', name
# def onWord(name, location, length):
#    print 'word', name, location, length
# def onEnd(name, completed):
#    print 'finishing', name, completed
#    if name == 'fox':
#       engine.say('What a lazy dog!', 'dog')
#    elif name == 'dog':
#       engine.endLoop()
# engine = pyttsx3.init()
# engine.connect('started-utterance', onStart)
# engine.connect('started-word', onWord)
# engine.connect('finished-utterance', onEnd)
# engine.say('The quick brown fox jumped over the lazy dog.', 'fox')
# engine.startLoop()

engine = pyttsx3.init()
engine.say('Sally sells seashells by the seashore.')
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait() 
