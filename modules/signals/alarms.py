import signal
import time

def receive_alarm(signum,stack):
    print('alarm',time.ctime())

signal.signal(signal.SIGALRM,receive_alarm)
signal.alarm(2)
print('before',time.ctime())
time.sleep(4)
print('after alarm',time.ctime())