import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "6f6861d1092442b2acfd6cd5688d6308"


def speak(text):
    # engine.stop() 
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    cmd = c.lower()
    if "google" in cmd:
        speak("Opening Google")
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
    
    elif "news" in c.lower():
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}"
        try:
            r = requests.get(url)

            # Check if request was successful
            if r.status_code == 200:
                data = r.json()
                articles = data.get("articles", [])

                if not articles:
                    print("No news found")
                    return

            # print the headline
                for article in articles[:5]:
                    print(article.get('title', 'No title'))

            else:
                print("Failed to fetch news")
            
        except Exception:
               print("Network error")
    

    # else:
        #Open Ai handling requests


if __name__ == "__main__":
    speak("----Initializing Jarvis----")

    speak("Jarvis is online")
    while True:
        #listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening.....")
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source, timeout=5, phrase_time_limit=5)

            word = r.recognize_google(audio)
            if "jarvis" in word.lower():
                speak("Yeah Master How it's going!")
                #listen for the command
                with sr.Microphone() as source:
                    print("Jarvis Activated..")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))

