def Add(Value1,Value2):
    
    Ans = 0
    Ans = Value1 + Value2
    return Ans

def main():
    
    print("Enter The First Number: ")
    No = int(input())
    
    print("Enter The Second Number: ")
    No1 = int(input())
    ret = 0
    
    
    ret = Add(No,No1)
    print("Addition is: ",ret)
    
if __name__ == "__main__":
    main()