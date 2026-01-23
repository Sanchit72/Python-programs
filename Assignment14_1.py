# Assignment14_1.py
# Write a program which contains one lambda function which accepts one number and return its square.

Square = lambda No: print(No * No)

    
def main():
    
    print("Enter The Number: ")
    Value = int(input())
    
    Square(Value)
     
if __name__ == "__main__":
    main()