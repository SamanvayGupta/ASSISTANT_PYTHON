import pyttsx3
import pyaudio
import speech_recognition as sr
import datetime
import webbrowser
import pywhatkit
import wikipedia
import os
import pyautogui

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voices',voices[0].id)
Assistant.setProperty('rate',190)

def speak(audio):
    print("   ")
    Assistant.say(audio)
    print(f": {audio}")
    print("   ")
    Assistant.runAndWait()
    
def Push_uI(a):
    f=open("D:\JARVIS\LOG_T.txt","a")
    if a!= "none":
        f.write(f"User: {a}")
        f.close()
    else:
        f.write("  ")
        f.close()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! Sir! How may i help you today.")

    elif hour>=12 and hour<18:
        speak("Good afternoon! Sir! How may i help you today.")

    else:
        speak("Good evening! Sir! How may i help you today.")

# speak(wishme())

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing....")
            query = command.recognize_google(audio,language='en-in')
            print(f"you said : {query}")

        except Exception as Error:
            return "none"
    return query.lower()

def functions_that_to_be_called():

    

    def OpenApps():
        speak("ok wait a bit")

        if 'WhatsApp' in query:
            speak("Here you go sir.")
            
            pyautogui.press("win")
            
            pyautogui.write("Whatsa")
            
            pyautogui.press("enter")
        



    while True:

        query = takecommand()
    

        if 'hello' in query:
            speak(" ")
            wishme()
            speak("")
            speak("")

        elif 'hi' in query:
            speak("HI there ")
            wishme()
            speak("I am Sia")
            speak("what to do now??")

        elif 'how are you' in query:
            speak("I am fine")
            speak("I am sure you are too")

        elif 'hello Sia' in query:
            speak("HI")
            wishme()
            speak("How are you")

        elif 'what is the meaning of Sia' in query:
            speak("there is no such meaning for that it just feel good so so i put name as Sia")
            speak("If you want you can put any name to me as your wish")

        elif 'yes' in query:
            speak("ok")
            speak("so what to do now")

        elif 'I am fine' in query:
            speak("Good to hear this sir.")
            speak("There is anything i can help you with")
            speak("or i should stand by")
        
            

        elif 'can you speak hindi too' in query:
            speak("not yet sir")
            speak("i can speak all the languages that are encoded in me")


        elif 'ok thats it' in query:
            speak("ok byee")
            speak("hope i was usefull")
            break

        elif 'youtube' in query:
            
            speak("Sure Sir.")
            query = query.replace("Sia","")
            query = query.replace("play","")
            query = query.replace("on youtube","")
            pywhatkit.playonyt(f"{query}")
            speak("Enjoy your video sir")
        
        elif "switch" or "switch tab" in query:
            speak("on your screen sir!")
            pyautogui.hotkey("alt","tab")
        
        elif "task manager" or "manager" in query:
            speak("hear you go sir")
            pyautogui.hotkey("ctrl","shift","esc")

        elif 'google' in query or "search" in query:
            speak("okk, this is what i found according to your words")
            query = query.replace("Sia","")
            query = query.replace("search","")
            query = query.replace("on google","")
            speak("done, hear you go")
            web = 'https://www.google.com/results?search_query=' + query
            speak("done sir, hear you go")


        elif 'launch a website' in query:
            speak("which website do you want me to launch!")
            name = takecommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            speak("hear you go with this")
            break

        elif 'play a song' in query:
            speak("okk")
            music()
            break

        elif 'play a video' in query:
            speak("okk")
            video()
            break

        elif 'wikipedia' in query:
            speak("speaking wikipedia........")
            query = query.replace("Sia","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            # print(wiki)
            speak(f"According to Wikipedia : {wiki}")
            break

        elif 'send message' in query:
            speak("ok")
            whatsaap()

        elif 'screenshot' in query:
            kk = pyautogui.screenshot()
            kk.save('D:\\')

        elif 'open youtube' in query:
            OpenApps()
            break

        # elif 'open WhatsApp' in query:
        #     OpenApps()
        #     break

        elif 'open pinterest' in query:
            OpenApps()
            break

        elif 'open instagram' in query:
            OpenApps()
            break

        elif 'open youtube' in query:
            OpenApps()
            break

        elif 'open map' in query:
            OpenApps()
            break

        elif 'open gmail' in query:
            OpenApps()
            break

        elif 'open chrome' in query:
            OpenApps()
            break

        else:
            speak("this was a in appropriate command")
functions_that_to_be_called()