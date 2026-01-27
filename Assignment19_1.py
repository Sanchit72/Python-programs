#Write a program which contains one lambda function whcih accepts one parameter and retrun power of two
#input4 = output=16,input6 = output64
Power = lambda No : 2 ** No

def main():
    
    No = int(input("Enter The Number: "))
    Ret = 0
    Ret = Power(No)
    print("Power is:",Ret )

if __name__ == "__main__":
    main()