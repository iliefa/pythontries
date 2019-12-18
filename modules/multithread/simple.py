#instantiate a thread with a target function and call start

import threading
import time

def worker():
    """thread worker function"""
    time.sleep(2)
    print('Worker')
 

threads=[]
for i in range(5):
    t=threading.Thread(target=worker) 
    threads.append(t)
    t.start()