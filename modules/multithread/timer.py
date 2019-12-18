#Timer included in threading
#starts its work after a delay, and can be canceled at any point 
# within the delay period

import threading
import logging
import time

def delayed():
    logging.debug('worker running')

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
)

t1 = threading.Timer(0.3,delayed)
t1.setName('timer1')
t2= threading.Timer(0.3,delayed)
t2.setName('timer2')
#second timer is never run
#first timer runs after the main program is done
#it is not a daemon thread,it is joined implicitly when the main thread is done
logging.debug('starting timers')
t1.start()
t2.start()
logging.debug('waiting before cancelling %s',t2.getName())
time.sleep(0.2)
logging.debug('cancelling %s',t2.getName())
t2.cancel()
logging.debug('done')