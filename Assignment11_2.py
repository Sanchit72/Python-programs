#write a program which contains one function named as DigitCount. That function should accept one number from user and print the count of digits in that number.

def DigitCount(Value):  
    count = 0
    while(Value != 0):
        Value = Value // 10
        count = count + 1
    print("Number of digits are:", count)
    
        
def main():
    
    print("Enter The Number: ")
    No = int(input())
    
    DigitCount(No)
    
if __name__ == "__main__":
    main()