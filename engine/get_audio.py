import speech_recognition as sr 

def get_audio():

    #It takes input from the user and returns string outputkes micropho

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('I am listening')
        r.phrase_time_limit=10
        audio = r.listen(source)

    try:   
        said = r.recognize_google(audio, language='en-us')
        print(f'Aaryan said: {said}\n')
    except: 
        return "None"
    return said