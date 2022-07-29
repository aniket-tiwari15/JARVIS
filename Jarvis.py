# pyttsx3 is a module that allows us to speak text in a voice format like Microsoft Speech Recognition API (MSRAPI) or Google Speech Recognition API (GSRAPI) or Amazon Speech Recognition API (ASRAPI).
import pyttsx3
# datetime is a module that allows us to get the current time.
import datetime

# take command from user function.
import speech_recognition as sr

# wikipedia function to search for a query in wikipedia.
import wikipedia

# sapi5 is the name of the voice that is used in the speak function above.

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# this print is just for check which type voice i have in my computer.
# print(voices[0].id)
# This function will take the voice that is selected in the computer and will speak the text that is passed to it.
engine.setProperty('voice', voices[0].id)


# Speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# wish me function
# This function will greet the user with the name of the user.
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. Please tell me how may I help you")  
    
# It takes microphone input from the user and returns string output. 
def takeCommand():
 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
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



if __name__=="__main__":
    # speak("Aniket is very powerful")
    wishMe()
    while True:
        query = takeCommand().lower()
        # Logic for executing tasks based on query 
        if 'wikipeadia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        # elif 'open youtube' in query:
        #     webbrowser.open("youtube.com")
        # elif 'open google' in query:
        #     webbrowser.open("google.com")
        # elif 'open stackoverflow' in query:
        #     webbrowser.open("stackoverflow.com")
        # # elif 'play music' in query:
        # #     music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
        # #     songs = os.listdir(music_dir)
        # #     print(songs)
        # #     os.startfile(os.path.join(music_dir, songs[0]))


