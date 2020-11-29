import sys
sys.path.insert(0, "/usr/lib/python3/dist-packages")
import notify2
import os

icon= os.getcwd()+'/engine/resources/main.jpg'


def notify(message,app=None):
    notify2.init("Dragon")

    if not app:
        notifier = notify2.Notification(f'Dragon' ,message,icon=icon)
    else:    
        notifier = notify2.Notification(f'Dragon - \"{app}\"',message,icon=icon)
    
    notifier.show()


