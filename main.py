import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open instagram" or "open insta" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    
   


if __name__ == "__main__":
    speak("Initilizing Shadow......")
    while True:
        #listen for wake word 'Shadow'
        #obtain audio from microphone
        r = sr.Recognizer()
       
    
    #recognize speech
        print("recognizing..")
        try:
            with sr.Microphone() as source:
                print("Listening.....")
                audio = r.listen(source,timeout=10, phrase_time_limit=10)
            word = r.recognize_google(audio)
            if(word.lower() == "hello"):
                speak("Yes")
                print("yes")
                #listen for command
                with sr.Microphone() as source: 
                    print("Shadow Activated.....")
                    audio = r.listen(source,timeout=10, phrase_time_limit=10)
                    command = r.recognize_google(audio)

                    processCommand(command)




        except Exception as e:
            print("error; {0}".format(e))
