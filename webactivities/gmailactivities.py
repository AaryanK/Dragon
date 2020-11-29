from __future__ import print_function
import smtplib
# from engine.speak import speak
import os
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request



SCOPES = ['https://mail.google.com/']

email_id = 'raysofrevolution@gmail.com'
email_id_password='sekyhvwgpyhbztio'
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(email_id, email_id_password)
    server.sendmail(email_id, to, content)
    return('email sent sucessfully')
    server.close()


def authenticate():
    creds = None
    if os.path.exists(f'{os.getcwd()}/webactivities/gmail.pickle'):
        with open(f'{os.getcwd()}/webactivities/gmail.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                f'{os.getcwd()}/webactivities/gmail.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open(f'{os.getcwd()}/webactivities/gmail.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    return service

def receivenewmessage(service=authenticate()):    
    global msg
    results= service.users().messages().list(userId="me",labelIds =['INBOX'],q="is:unread").execute()
    messages=results.get('messages', [])

    for message in messages:
        msg = service.users().messages().get(userId="me",id =message['id']).execute()
        no_of_messages = 0

        if messages:
            for message in messages:
                msg = service.users().messages().get(userId="me",id =message['id']).execute()
                no_of_messages=no_of_messages+1
                email_data=msg['payload']['headers']
                for values in email_data:
                    name=values["name"]
                    if name=="From":
                        From_name=values["value"]
                        return f'new message received from {From_name}'

print(receivenewmessage())