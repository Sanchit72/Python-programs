# wirte a progrm which accept number from user return addition of digit in that numeber

def Sum(No):
    Digit = 0
    Sum = 0
    while(No != 0):
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10
    return Sum

def main():
    
    No = int(input("Enter Number: "))
    
    Ret = Sum(No)
    print("Addition of digits is:", Ret)
    
if __name__ == "__main__":
    main()
