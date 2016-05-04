import speech_recognition as sr
import pyttsx

r = sr.Recognizer()
m = sr.Microphone()

def speak(value):
    engine = pyttsx.init()
    engine.say(value)
    engine.runAndWait()

def record():
    print("Hey Buddy! say Something..")
    with m as source:
        audio = r.listen(source)
    print("Got it! Let me interprett it....")
    return audio

def interpret(audio):
    try:
        # recognize speech using Google Speech Recognition
        value = r.recognize_google(audio)
        return value
    except sr.UnknownValueError:
        value = "I did not understand it"
        return value
    except sr.RequestError as e:
        value = "Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e)
        return value
    
def write(value):
    # we need some special handling here to correctly print unicode characters to standard output
    if str is bytes: # this version of Python uses bytes for strings (Python 2)
        print(u"Did you say: {}".format(value).encode("utf-8"))
    else: # this version of Python uses unicode for strings (Python 3+)
        print("Did you say: {}".format(value))

def main():
    r = sr.Recognizer()
    m = sr.Microphone()
    try:
        print("A moment of silence, please...")
        with m as source:
            r.adjust_for_ambient_noise(source)
            print("Minimum energy threshold set to {}".format(r.energy_threshold))
    
        while True:
                
            speak("Whats up! Say something..")
            audio = record()
            value = interpret(audio)
            speak(value)
            write(value)

    except KeyboardInterrupt:
        speak("Good Bye!")
        pass
if __name__ == '__main__':
    main()
