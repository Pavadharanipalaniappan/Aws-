import threading
import time
from queue import Queue

def worker(queue, thread_num):
    while True:
        job = queue.get()
        if job is None:
            break
        print(f"Thread {thread_num} started job {job}")
        time.sleep(job)
        print(f"Thread {thread_num} finished job {job}")
        queue.task_done()

# Create a queue of jobs
job_queue = Queue()

# Add jobs to the queue
jobs = [2, 4, 1, 3, 5, 0]
for job in jobs:
    job_queue.put(job)

# Create and start the worker threads
num_threads = 3
threads = []
for i in range(num_threads):
    t = threading.Thread(target=worker, args=(job_queue, i))
    t.start()
    threads.append(t)

# Wait for all jobs to be completed
job_queue.join()

# Stop the worker threads
for i in range(num_threads):
    job_queue.put(None)
for t in threads:
    t.join()