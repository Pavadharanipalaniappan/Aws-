import threading
def print_thread_name():
    print(f"Thread {threading.current_thread().name} is running")
thread1 = threading.Thread(target=print_thread_name, name="Thread-1")
thread2 = threading.Thread(target=print_thread_name, name="Thread-2")
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("All threads have finished.")