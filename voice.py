import time
import speech_recognition as sr #convert speech to text
import datetime #for fetching date and time
#import wikipedia
import webbrowser
import requests
from playsound import playsound # to play saved mp3 file
import wikipedia as wikipedia
from gtts import gTTS # google text to speech 
import os # to save/open files 
import wolframalpha # to calculate strings into formula
from selenium import webdriver # to control browser operations

def talk():
    input=sr.Recognizer()
    with sr.Microphone() as source:
        audio=input.listen(source)
        data=""
        try:
            data=input.recognize_google(audio)
            print("Your question is, " + data)
            
        except sr.UnknownValueError:
            print("Sorry I did not hear your question, Please repeat again.")
#return data
def respond(output):
    num=0
    print(output)
    num += 1
    response=gTTS(text=output, lang='en')
    file = str(num)+".mp3"
    response.save(file)
    #playsound.playsound(file, True)
    #file('1.mp3')
    os.remove(file)
def speechtotext(duration):
    global i, addr, passwrd
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=3)
        # texttospeech("speak", file + i)
        # i = i + str(1)
        #playsound('speak.mp3')
        audio = r.listen(source, phrase_time_limit=3)
    try:
        response = r.recognize_google(audio)
    except:
        response = 'N'
    return response
if __name__=='__main__':
    respond("Hi, I am voice assist your personal desktop assistant")
          
    while(1):
        respond("How can I help you?")
        #text=talk().lower()
        text = speechtotext(5).lower()
        print (text)
        if text==0:
            continue
            
        if "stop" in str(text) or "exit" in str(text) or "bye" in str(text):
            respond("Ok bye and take care")
            break
            
        #if 'wikipedia' in text:
        #     respond('Searching Wikipedia')
        #     text =text.replace("wikipedia", "")
        #     results = wikipedia.summary(text, sentences=3)
        #     respond("According to Wikipedia")
        #     print(results)
        #     respond(results)
        elif 'time' in text:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            respond(f"the time is {strTime}")

        elif 'search' in text:
            text = text.replace("search", "")
            webbrowser.open_new_tab(text)
            time.sleep(5)

        elif 'word' in text:
            print("working")
            respond("Opening Microsoft Word")
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word 2016')
            time.sleep(5)

        elif 'excel' in text:
            print("working")
            respond("Opening Microsoft Word")
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel 2016')
            time.sleep(5)

        elif 'powerpoint' in text:
            print("working")
            respond("Opening Microsoft Word")
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint 2016')
            time.sleep(5)

        elif 'youtube'  in text:
            # text = text.replace("search", "")
            # webbrowser.open_new_tab(text)
            # time.sleep(5)
            webbrowser.open_new_tab("https://www.youtube.com")
            respond("youtube is open")
            time.sleep(5)

        elif 'control panel'  in text:
            text = text.replace("control panel", "")
            webbrowser.open_new_tab(text)
            time.sleep(5)
        

        elif 'google' in text:
            print("working")
            webbrowser.open_new_tab("https://www.google.com")
            respond("Google is open")
            time.sleep(5)
            
        elif 'youtube1' in text:
            driver = webdriver.Chrome(r"Mention your webdriver location") 
            driver.implicitly_wait(1) 
            driver.maximize_window()
            respond("Opening in youtube") 
            indx = text.split().index('youtube') 
            query = text.split()[indx + 1:] 
            driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query))              
                
        elif "word1" in text:
            print("working")
            respond("Opening Microsoft Word")
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word 2016')
        
        else:
           respond("Application not available")
