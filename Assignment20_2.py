# Design a python application create two thread nameed EvenFactor and OddFactor.both thread accept one integer number as parameter the evenfactor thread should calculate sum of even factor of that number and sum of oddfactor thread should calculate odd factor of that number.after the execution main thread should display the meassage  exit from main

import threading
import time

def even_factor(number):
    even_sum = 0
    for i in range(1, number + 1):
        if number % i == 0 and i % 2 == 0:
            even_sum += i
    print(f"Sum of even factors of {number} is: {even_sum}")
    time.sleep(1)
def odd_factor(number):
    odd_sum = 0
    for i in range(1, number + 1):
        if number % i == 0 and i % 2 != 0:
            odd_sum += i
    print(f"Sum of odd factors of {number} is: {odd_sum}")
    time.sleep(1)
def main():
    number = int(input("Enter an integer number: "))
    
    even_thread = threading.Thread(target=even_factor, args=(number,))
    odd_thread = threading.Thread(target=odd_factor, args=(number,))
    
    even_thread.start()
    odd_thread.start()
    
    even_thread.join()
    odd_thread.join()
    
    print("Exit from main")