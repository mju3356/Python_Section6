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
t2=threading.Thread(name='Service-2',target=worker2)
t3=threading.Thread(target=worker2)

if __name__=='__main__':
    t1.start()
    t2.start()
    t3.start()
    print('t3 : isAlive()',t3.isAlive())
    #Join 메소드 호출로 쓰레드 종료시 까지 대기
    t1.join() #join() 시간 동안 대기
    t2.join()
    t3.join()
