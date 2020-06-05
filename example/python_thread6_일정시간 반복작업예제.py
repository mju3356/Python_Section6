#일정 시간 간격으로 반복 작업가능한 예제
import time
import threading

def thread_run():
    print('======',time.ctime(),'======')
    #개발 하고자 하는 코드

    for i in range(1,11):
        print('Threading Runing - ',i)
    threading.Timer(5,thread_run).start()

thread_run()
