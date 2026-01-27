# Design a python application that create two thread named evenlist and oddlist accept list of integers as input from user and the evenlist thread should display all even numbers from the list and oddlist thread should display all odd numbers from the list.after the execution main thread should display the message exit from main
import threading

def even_list(num):
    even_numbers = [n for n in num if n % 2 == 0]
    print(f"Even numbers: {even_numbers}")
    
def odd_list(num):
    even_numbers = [n for n in num if n % 2 != 0]
    print(f"Odd numbers: {even_numbers}")
    

def main():
    numbers = list(map(int, input("Enter a list of integers separated by space: ").split()))
    
    even_thread = threading.Thread(target=even_list, args=(numbers,))
    odd_thread = threading.Thread(target=odd_list, args=(numbers,))
    
    even_thread.start()
    odd_thread.start()
    
    even_thread.join()
    odd_thread.join()
    
    print("Exit from main")
    
if __name__ == "__main__":
    main()