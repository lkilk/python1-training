from threading import Thread, Lock
from concurrent.futures import ThreadPoolExecutor 
import time

counter = 0
lock = Lock()

def increment(id):
    global counter
    lock.acquire()
    x = counter
    x += 1
    time.sleep(0.5)
    counter = x
    lock.release()
    print(f"Thread {id} completed")

# threads = []

# for i in range(10):
#     t = Thread(target=increment)
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()

lst = [1,2,3,4,5,6,7,8,9,10]
# exec = ThreadPoolExecutor()
# exec.map(increment, )

with ThreadPoolExecutor() as exec:
    exec.map(increment, lst)

print(counter)
