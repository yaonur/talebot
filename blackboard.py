import threading
import time


def a():
    while True:
        print('a')
        time.sleep(1)
def b():
    while True:
        print('b')
        time.sleep(1)
def c():

    while True:
        print('c')
        time.sleep(1)

thebel=threading.Thread(target=a)
thubel=threading.Thread(target=b)
thebel.start()
thubel.start()
c()