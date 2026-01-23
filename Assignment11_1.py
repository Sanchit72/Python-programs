#

def PrimeNumber(Value):
    flag = False
    for i in range(2, (Value//2)+1): 
        if(Value % i == 0):
            flag = True
            break
    
def main():
    
    flag = False
    print("Enter The Number: ")
    No = int(input())
    
    PrimeNumber(No)

    if flag == False:
        print("Prime Number")
    else:
        print("Not Prime")
    
if __name__ == "__main__":
    main()