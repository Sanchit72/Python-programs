def reversed(Value):
    rev = 0
    while(Value != 0):
        digit = Value % 10
        rev = Value * 10 + digit
        Value = Value // 10
    return rev
    
def main():
    
    print("Enter The Number: ")
    No = int(input())
    ret = 0
    
    ret =  reversed(No)
    
    print("Reversed Number is:", ret)
if __name__ == "__main__":
    main()