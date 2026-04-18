import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    # engine.stop() 
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com/")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open mail" in c.lower():
        webbrowser.open("https://www.gmail.com/")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com/")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
        

if __name__ == "__main__":
    speak("----Initializing Jarvis----")

    speak("Jarvis is online")
    while True:
        #listen for the wake word "Isabella"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening.....")
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source, timeout=5, phrase_time_limit=5)

            word = r.recognize_google(audio)
            if "jarvis" in word.lower:
                speak("Yeah Master How it's going!")
                #listen for the command
                with sr.Microphone() as source:
                    print("Jarvis Activated..")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))

