import threading
import time
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)


def worker():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')


t = threading.Thread(name='worker', target=worker)
t.start()

t.join(1)
print('t.is_alive()', t.is_alive())
t.join()
print('t.is_alive()', t.is_alive())