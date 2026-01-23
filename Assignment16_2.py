def ChkNum(Value):
    if(Value % 2 ==0):
        print("Even Number")
    else:
        print("Odd Number")

def main():
    
    print("Enter The Number: ")
    No = int(input())
    
    ChkNum(No)
    
if __name__ == "__main__":
    main()
    