# Write a python application that create two thread named thread1 and thread2 . thread1 display number from 1 to 50 thread2 should display number from 50 to 1 reverse order.

import threading

def DisplayAscending():
    for i in range(1, 51):
        print("Thread 1 - Ascending:", i)
        
def DisplayDescending():
    for i in range(50, 0, -1):
        print("Thread 2 - Descending:", i)
        
def main():
    print("Main thread started")
    
    thread1 = threading.Thread(target=DisplayAscending)
    thread2 = threading.Thread(target=DisplayDescending)
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    print("Main thread completed")
    
if __name__ == "__main__":
    main()