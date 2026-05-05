import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import os
newsapi = os.getenv("NEWS_API_KEY")

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    # engine.stop() 
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    cmd = c.lower()

    if any(x in cmd for x in ["end jarvis","stop jarvis", "exit",'quit']):
        print("Shutting down Jarvis.....")
        return False


    elif "google" in cmd:
        print("Opening Google")
        webbrowser.open("https://www.google.com/")
    elif "youtube" in cmd:
        print("Opening Youtube")
        webbrowser.open("https://www.youtube.com/")
    elif "mail" in cmd:
        print("Opening Gmail")
        webbrowser.open("https://www.gmail.com/")
    elif "linkedin" in cmd:
        print("Opening LinkdIn")
        webbrowser.open("https://www.linkedin.com/")
    elif cmd.startswith("play"):
        parts = cmd.split(" ")

        if len(parts) < 2:
            print("NO Song Specified")
            return True
        
        song = " ".join(parts[1:])
        link = musicLibrary.music.get(song)

        if link:
            webbrowser.open(link)
        else:
            print("Song Not Found")
    
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
    

    else:
        #Open Ai handling requests
        pass


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

                    should_countinue = processCommand(command)

                    if should_countinue is False:
                        break
                    # processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))

