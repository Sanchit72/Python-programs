# write program which accept one number from user and return its prime or not

def Prime(No):
    if No <= 1:
        return False
    for i in range(2, int(No**0.5) + 1):
        if No % i == 0:
            return False
    return True

def main():
    No = int(input("Enter Number: "))
    
    Ret = Prime(No)
    if Ret == True:
        print(f"{No} is a prime number")
    else:
        print(f"{No} is not a prime number")
        
if __name__ == "__main__":
    main()