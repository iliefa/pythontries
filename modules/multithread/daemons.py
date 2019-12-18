"""
daemon=thread that runs without blocking the main program from exiting
when it's not an easy way to interrupt the thread
where letting the thread die in the middle of the work does not lose data
heart beats daemon
pass daemon=True
"""
import threading
import time
import logging


def daemon():
    logging.debug('Starting')
    time.sleep(0.2)
    logging.debug('Exiting')


def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

d = threading.Thread(name='daemon', target=daemon, daemon=True)

t = threading.Thread(name='non-daemon', target=non_daemon)
""" join is used to wait until a daemon thread has completed it's work
otherwise the output will not include "exiting" from the daemon thread
-all of the non-daemon threads exit before the daemon thread wakes up from the sleep call
"""
d.start()
t.start()
d.join()
t.join()