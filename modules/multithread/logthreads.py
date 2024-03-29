#embedd the thread name in every log message using %(threadName)s

import logging
import threading
import time

def worker():
    logging.debug('starting')
    time.sleep(2)
    logging.debug('exiting')

def my_service():
    logging.debug('starting')
    time.sleep(3)
    logging.debug('Exiting')

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
)

t = threading.Thread(name='my_service',target=my_service)
w = threading.Thread(name='worker',target=worker)
w2= threading.Thread(target=worker)

w.start()
w2.start()
t.start()