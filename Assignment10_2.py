def sumNatural(No):
    sum = 0
    for i in range(1,No+1):
        sum = sum + i
    return sum
            
            

    
def main():
    
    print("Entr The number:")
    No = int(input())
    result = 0
    
    result=sumNatural(No)
    
    print("Sum of natural number is :",result)
    
if __name__ == "__main__":
    main()
    