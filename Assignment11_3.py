def SumDigit(Value):
    sum = 0
    while(Value != 0):
        digit = Value % 10
        sum = sum + digit
        Value = Value // 10
    return sum

def main():
    
    print("Enter The Number: ")
    No = int(input())
    ret = 0
    
    ret = SumDigit(No)
    
    print("Sum of digits is:", ret)
    
if __name__ == "__main__":
    main()