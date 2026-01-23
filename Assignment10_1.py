#write a program which contains one function named as Multiplication. That function should accept one number from user and print multiplication of that number.

def Multiplication(Value):
    for i in range(1,11):
        print(Value * i)
        

def main():
    
    print("Enter The Number: ")
    No = int(input())
    result = 0
    
    Multiplication(No)
    
    
if __name__ == "__main__":
    main()