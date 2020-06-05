import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s (%(threadName)-8s) %(message)s]',

)

def worker1():
    logging.debug('Starting')
    time.sleep(0.5)
    logging.debug('Exiting')

def worker2():
    logging.debug('Starting')
    time.sleep(0.5)
    logging.debug('Exiting')
#데몬쓰레드 :(옵션 생략시 기본 쓰레드)
t1=threading.Thread(name='Service-1',target=worker1)
t2=threading.Thread(name='Service-2',target=worker2,daemon=True)
t3=threading.Thread(target=worker2,daemon=True)

t1.start()
t2.start()
t3.start()
