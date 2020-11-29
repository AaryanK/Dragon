from engine.speak import speak 
from engine.get_audio import get_audio
import datetime
import threading
from clock.alarm import morning_alarm
from clock.weather import weather_info,weather_at_place
import webbrowser
from graphics import guis
from clock.notification import notify
from webactivities import gmailactivities as ga
from engine.makethreads import make_thread
from engine.makeprocesses import make_processes,execute

good_morning_tags=['morning dragon','good morning','good morning dragon','hey good morning']
wake_up_time='05:00'
a = make_thread(morning_alarm,args=(wake_up_time,))

if __name__ == "__main__":
    while True:
        text =get_audio().lower()

        if text in good_morning_tags:
            speak('Good Morning Sir.!')
            outside = weather_info()
            speak(f'It is {outside} degree centigrede outside') 

        if "open discord" in text:
            speak("Opening Discord")
            webbrowser.open_new_tab("http://discord.com/app")

        if "send a message" in text:
            speak("Okay sir,please write the mail address you want to send to.")
            to =execute(guis.popupmessage,'Whom to send ?') 
            print(to)
            speak("Okay sir what should I write? ")
            content=f'{get_audio()}\n\n\n(sent from Dragon)'
            try:
                notify(ga.sendEmail(to,content),'Email')
            except Exception as e:
                print(e)
                print("was an error sir plz try again.")
        
        if "what is the weather in" in text:
            text = text.split()
            print(text)
            text = text[5]
            speak(f'{weather_at_place(text)} degree centrigredes')
            
