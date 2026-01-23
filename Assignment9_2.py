#write a program which contains one function named as CkkGreater.# That function should accept two numbers from user and return greater number.# Input : 10  11 # Output : 11

def CkkGreater(value1,value2):
    if(value1 > value2):
        return value1
    else:
        return value2
    

def main():
    
    print("Enter First Number: ")
    No1 = input()
    print("Enter Second Number: ")
    No2 = input()
    ret = 0
    
    ret = CkkGreater(No1,No2)
    
    print("Greater is",ret)
    
    
if __name__ == "__main__":
    main()
    