import os
import time
os.environ.__setitem__('DISPLAY', ':0.0')

import PySimpleGUI as sg

'''puplayout = [[sg.Text(""),key="first"],
                [sg.Input(""),key="finput"]]
'''
def popupmessage(messagetodisplay,title=None,character=None,bgcolour=None,texttoshow=None,time=None):
    result = sg.popup_get_text(message=messagetodisplay,password_char=character,default_text=texttoshow,modal=False)
    return result    

