# write a program acceppt one number from user and return its factorial
def Factorial(No):
        Fact = 1
        for i in range(1, No + 1):
            Fact = Fact * i
        return Fact
def main():
    No = int(input("Enter Number: "))
    
    Ret = Factorial(No)
    print("Factorial is:", Ret)
    
if __name__ == "__main__":
    main()