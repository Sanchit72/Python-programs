# wirte a progrm which accept number from user return digit in that number

def Count(No):
    Digit = 0
    while(No != 0):
        No = No // 10
        Digit = Digit + 1
    return Digit

def main():
    No = int(input("Enter Number: "))
    
    Ret = Count(No)
    print("Number of digits are:", Ret)
    
if __name__ == "__main__":
    main()