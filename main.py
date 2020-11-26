from engine.speak import speak 
from engine.get_audio import get_audio
import datetime
import threading
from clock.alarm import morning_alarm
from clock.weather import weather_info,weather_info
import webbrowser

good_morning_tags=['morning dragon','good morning','good morning dragon','hey good morning']
wake_up_time='17:34'
alarmthread = threading.Thread(target=morning_alarm, args=(wake_up_time,))

if __name__ == "__main__":
    alarmthread.start()
    while True:
        text =get_audio().lower()

        if text in good_morning_tags:
            speak('Good Morning Sir.!')
            outside = weather_info()
            speak(f'It is {outside} degree centigrede outside') 

        if "open discord" in text:
            speak("Opening Discord")
            webbrowser.open_new_tab("http://discord.com/app")
