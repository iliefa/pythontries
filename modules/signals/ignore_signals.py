import signal
import os
import time

def do_exit(sig,stack):
    raise SystemExit('i will exit')
#register SIG_IGN as the handler 
#ignores sigint(ctrl +c ) and raises systemexit when it sees sigusr1
signal.signal(signal.SIGINT,signal.SIG_IGN)
signal.signal(signal.SIGUSR1,do_exit)
#kill -USR1 and pid to stop the process
print('my pid',os.getpid())
signal.pause()