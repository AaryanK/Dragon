from graphics import guis
from engine.makeprocesses import execute
from clock.notification import notify
from webactivities import gmailactivities as ga

to =execute(guis.popupmessage,'Whom to send ?') 
print(to)
content=f'hey\n\n\n(sent from Dragon)'
try:
    notify(ga.sendEmail(to,content),'Email')
except Exception as e:
    print(e)
    print("was an error sir plz try again.")

