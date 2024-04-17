import threading
import time


def worker():
    print(threading.current_thread().name, 'Starting')
    time.sleep(2)
    print(threading.current_thread().name, 'Exiting')

def my_service():
    print(threading.current_thread().name, 'Starting')
    time.sleep(3)
    print(threading.current_thread().name, 'Exiting')


t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker)  # use default name

w.start()
w2.start()
t.start()