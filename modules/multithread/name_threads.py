import threading
import time

def worker():
    print(threading.currentThread().getName(),'starting')
    time.sleep(1)
    print(threading.currentThread().getName(),'exiting')

def my_service():
    print(threading.currentThread().getName(),'starting')
    time.sleep(2)
    print(threading.currentThread().getName(),'exiting')

t=threading.Thread(name='my_service',target=my_service)
w=threading.Thread(name='worker',target=worker)
w2=threading.Thread(target=worker) #use default name

w.start()
w2.start()
t.start()