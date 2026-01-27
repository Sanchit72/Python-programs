# Design a python application where multiple thread update a shared variable use a lock to avoid race condition each thread should incremant the shared counter multiple times display the final value of the counter after all thread complete execution

import threading


counter = 0
counter_lock = threading.Lock()
def increment_counter(num_increments):
    global counter
    for _ in range(num_increments):
        with counter_lock:
            counter += 1
def main():
    global counter
    num_threads = 5
    increments_per_thread = 100000
    
    threads = []
    
    for _ in range(num_threads):
        thread = threading.Thread(target=increment_counter, args=(increments_per_thread,))
        threads.append(thread)
        thread.start()
        
    for thread in threads:
        thread.join()
        
    print("Final counter value:", counter)
    
if __name__ == "__main__":
    main()