import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from googletrans import Translator


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    # it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold=1
        r.pause_threshold = 0.6  # Adjust this value as needed
        r.energy_threshold = 4000  # Adjust this value as needed
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

# Not using my email and password for security issues


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo
    server.starttls()
    server.login('your-email@gmail.com', 'your-password')
    server.sendmail('your-email@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()

        if 'iris switch back' in query:
            engine = pyttsx3.init('sapi5')
            voices = engine.getProperty('voices')
            # print(voices[0].id)
            engine.setProperty('voice', voices[0].id)
            speak('Jarvis here Sir!')

        if not 'jarvis' in query:
            continue

        if 'switch' in query:
            engine = pyttsx3.init('sapi5')
            voices = engine.getProperty('voices')
            # print(voices[0].id)
            engine.setProperty('voice', voices[1].id)
            speak('Hello there. I am Iris at your service master')

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'open chat gpt' in query:
            webbrowser.open("https://www.openai.com")

        elif 'open git' in query:
            webbrowser.open("https://www.github.com")

        elif 'play music' in query:
            music_dir = ''
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'open discord' in query:
            discPath = "C:\\Users\\OMEN\\AppData\\Local\\Discord\\app-1.0.9012\\Discord.exe"
            os.startfile(discPath)

        elif 'open code' in query:
            codePath = "C:\\Users\\OMEN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open honkai' in query:
            honkPath = "E:\\Honkai Impact 3rd glb\\launcher.exe"
            os.startfile(honkPath)

        elif 'email to myself' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "your-email@gmail.com"  # your email goes here
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send this email")

        elif 'translate' in query:
            try:
                speak("Please provide me with the passage you want to translate Sir.")
                passage = input("Enter your passage: ")
                translator = Translator()
                translation = translator.translate(passage)
                translated_text = translation.text
                print(translated_text)
                speak(translated_text)
            except Exception as e:
                print(e)
                speak("Sorry Sir, could not translate it.")
