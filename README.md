Jarvis Voice Assistant (Python)

A simple voice-controlled assistant built using Python that can open websites, play music, and fetch the latest news using voice commands.

 Features : 
            Voice recognition using microphone
            Open websites like Google, YouTube, Gmail, LinkedIn
            Play songs from a custom music library
            Fetch and display latest news headlines
            Exit command ("end jarvis", "stop jarvis", etc.)

How It Works :
            Listens for the wake word "Jarvis"
            Captures your voice command
            Converts speech → text
            Executes the corresponding action
Technologies Used :
            SpeechRecognition – for voice input
            pyttsx3 – for text-to-speech
            requests – for fetching news data
            webbrowser – to open websites
            os – for environment variables

Run the Project :
            python main.py

Example Commands : 
            "Jarvis open Google"
            "Jarvis open YouTube"
            "Jarvis play perfect"
            "Jarvis news"
            "Jarvis end jarvis"

Notes :
            Requires a working microphone
            Internet connection needed for speech recognition and news
            Songs are played via YouTube links

Future Improvements :
            Add AI-based responses
            Improve natural language understanding
            GUI interface
            Dynamic music search
    
License : 
            This project is for educational purposes.

Acknowledgment : 
            Built as a learning project to understand speech recognition, APIs, and automation using Python.
