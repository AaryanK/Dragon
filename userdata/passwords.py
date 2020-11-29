import json
import os

class passwords:
    def __init__(self,mp):
        self.mp=mp

    def checkmp(self):
        if self.mp=='Aaryan0325':
            return 'Logged on successfully'
        else:
            return 'You are not authorized to snoop in Aaryan\'s credentials'

    
    def dump(self,appname,username,password):
        '''self.appname=appname
        self.username=username
        self.password=password'''
        data = {appname.lower(): {
        "username": username,
        "password": password
    }}
    
        file = open(f'{os.getcwd()}/userdata/credentials.json','r+')
        fil =json.load(file)
        appname = appname.lower()
        if appname in fil:
            while True:
                ans = input(f"The credentials of {appname} has already been added to my database do you want to update it? (Y/n) : ")
                if ans.lower()=='y' or ans.lower()=='yes':
                    file.close()
                    file1 = open(f'{os.getcwd()}/userdata/credentials.json','w+')
                    fil[appname]["username"] = username
                    fil[appname]["password"] = password
                    break
                if ans.lower()=='n' or ans.lower()=='no':
                    return('Okay')
                    pass
                    quit()
                else:
                    return("please try again")
        # file = open(f'{os.getcwd()}/userdata/credentials.json','w+')
        fil.update(data)
        try:
            file.seek(0)
        except:
            pass
        try:
            json.dump(fil,file1)
        except:
            json.dump(fil,file)

        try:
            file1.close()
        except:
            file.close()

    def exit(self):
        return 'windows'

    def showcreds():
        a = open(f"{os.getcwd()}/userdata/credentials.json",'r+')
        a=json.load(a)
        def showapps():
            apps = []
            for apps in a:
                apps.append(apps)
            # def showusernamepasswords():        
                
            print("Username: ",a[apps]['username'])
            print("Password: ",a[apps]['passsword'])
            print('-----------------------------')
    
'''a=passwords(mp='Aaryan0325')
print(a.checkmp())
a.dump('duckduckgo','aaryan','333')'''