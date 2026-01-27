#Write a program which contains one lambda function whcih accepts two parameter and retrun its multiplication

Mult = lambda No1,No2 : No1 * No2 

def main():
    
    No1 = int(input("Enter The Number: "))
    No2 = int(input("Enter The Number: "))
    Ret = 0
    Ret = Mult(No1,No2)
    print("Power is:",Ret )

if __name__ == "__main__":
    main()