# write a python application create three thread named Small,Capital and Digits. all accept string as input from user and small thread count and display number of lowercase characters from the string, capital thread count and display number of uppercase characters from the string and digits thread count and display number of digits from the string.after the execution main thread should display the message exit from main each thread must also dispaly  thread id and thread name

import threading
def count_lowercase(s):
        lowercase_count = sum(1 for char in s if char.islower())
        print(f"[{threading.current_thread().name}] (ID: {threading.get_ident()}) - Lowercase characters: {lowercase_count}")

def count_uppercase(s):
        uppercase_count = sum(1 for char in s if char.isupper())
        print(f"[{threading.current_thread().name}] (ID: {threading.get_ident()}) - Uppercase characters: {uppercase_count}")

def count_digits(s):
        digit_count = sum(1 for char in s if char.isdigit())
        print(f"[{threading.current_thread().name}] (ID: {threading.get_ident()}) - Digits: {digit_count}")

def main():
    
    user_input = input("Enter a string: ")

    small_thread = threading.Thread(target=count_lowercase, args=(user_input,), name="Small")
    capital_thread = threading.Thread(target=count_uppercase, args=(user_input,), name="Capital")
    digits_thread = threading.Thread(target=count_digits, args=(user_input,), name="Digits")

    small_thread.start()
    capital_thread.start()
    digits_thread.start()

    small_thread.join()
    capital_thread.join()
    digits_thread.join()

    print("Exit from main")
    
if __name__ == "__main__":
    main()
    