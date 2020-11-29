import threading
import sys

def make_thread(func,args=None):
    t=threading.Thread(target=func,args=args)
    t.start()    
