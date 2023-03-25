import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may I help you")        


def takeCommand():
    #it takes microphone input from the user and returns string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query        

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if not 'jarvis' in query:
            continue

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("Wikipedia", "")
            results=wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open chat gpt' in query:
            webbrowser.open("openai.com")

        elif 'open git' in query:
            webbrowser.open("github.com")    

        elif 'play music' in query:
            music_dir=''
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
            honkPath="E:\\Honkai Impact 3rd glb\\launcher.exe"
            os.startfile(honkPath)       

        # elif 'email to myself' in query:
            # try:
                # speak("What should I say")                 

                           

    
