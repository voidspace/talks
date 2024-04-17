import threading
import time
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)


def thread():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')


t = threading.Thread(name='worker', target=thread)

t.start()
t.join()