import signal
import os
import time

def receive_signal(signum,stack):
    print('received',signum)

signal.signal(signal.SIGUSR1, receive_signal)
signal.signal(signal.SIGUSR2,receive_signal)
print('my pid is ',os.getpid())
while True:
    print('waiting..')
    time.sleep(3)