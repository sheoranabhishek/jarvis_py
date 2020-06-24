import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')  # microsoft speech api
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

# setting speech rate.
# getting details of current speaking rate  # printing current voice rate
rate = engine.getProperty('rate')
engine.setProperty('rate', 160)


# speech function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    # print(hour)
    if hour >= 0 and hour <= 12:
        speak("Subh ki Ram Ram , Hello Sheoran , How May I Help You ?")
    elif hour >= 12 and hour < 18:
        speak("Dophr ki Ram Ram , Hello Sheoran , How May I Help You ?")
    else:
        speak("Sham ki Ram Ram , Hello Sheoran , How May I Help You ?")


def takeCommand():
    # it take microphone input from user , and returns string output
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        # print(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said : {query}\n")

    except Exception as e:
        print(e)
        print("I couldn't hear it . Please say it correctly.")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    # logic for executing tasks based on queries.

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia ... ')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif '.com' in query:
            webbrowser.get(chrome_path).open('youtube.com')
