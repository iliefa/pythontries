#create subclasses of thread
import logging
import threading

class MyThread(threading.Thread):
    def run(self):
        logging.debug('runing')

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

for i in range(5):
    t = MyThread()
    t.start()