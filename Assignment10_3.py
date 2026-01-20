def Factorial(No):
    Fact = 1
    for i in range(1,No+1):
        Fact = Fact * i
    return Fact
            
            

    
def main():
    
    print("Entr The number:")
    No = int(input())
    result = 0
    
    result=Factorial(No)
    
    print("Factorial is :",result)
    
if __name__ == "__main__":
    main()
    