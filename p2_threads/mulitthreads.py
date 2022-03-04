from threading import Thread
import time


def sleeper(id):
    time.sleep(3)
    print(f"Thread {id} completed task")


# t1 = Thread(target=sleeper, args=(1,)) #requires a tuple, hence teh commer after the argument
# t2 = Thread(target=sleeper, args=(2,))
# t3 = Thread(target=sleeper, args=(3,))


# t1.start()
# t2.start()
# t3.start()

threads = []

start_time = time.perf_counter()

for i in range(10):
    t = Thread(target=sleeper, args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    t.join() 

end_time = time.perf_counter()

print(end_time - start_time)


print(f"End of main thread")