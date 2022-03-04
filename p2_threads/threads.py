from threading import Thread
import time

#1. Method: Thread(target=callable) callable :function or Instance of a class
#2. Method: Subclassing Thread and overriding its run()

# Method 1a : Thread(target=func)

def sleeper():
    time.sleep(1)
    print(f"Thread completed task")

# thread = Thread(target=sleeper)
# thread.start()

class MyCallable: 

    def __init__(self):
        pass

    def __call__(self):
        time.sleep(1)
        print(f"thread is done")

my_callable = MyCallable()
# my_callable() #my_callable.__call__

thread = Thread(target=my_callable())
thread.start()

# Method 3 : Subclassing Thread and overriding its run() 

class AThread(Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        time.sleep(2)
        print(f"Ahh, the hard work is done")

athread = AThread() 
athread.start()
         
print(f"The END")

