import datetime
from pydub import AudioSegment
from pydub.playback import play
from engine.speak import speak
import os
import time

def morning_alarm(alarmtime):
    while True:
        tim = datetime.datetime.now().strftime('%H')+':'+datetime.datetime.now().strftime('%M')
        if tim == alarmtime:
                music = AudioSegment.from_mp3(os.getcwd()+'/clock/resources/m.mp3')
                for i in range(3):
                	play(music)
                	speak(f'Good morning sir Its {tim} now!')

     

            
