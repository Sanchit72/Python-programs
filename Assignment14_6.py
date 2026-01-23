# Functional

#def CheckEven(No):    
   # return(No % 2 != 0)
   
CheckOdd = lambda No : (No % 2 != 0)
       
def main():
    Value = 0
    Ret = False
    
    print("Enter Number:")
    Value = int(input())
    
    Ret = CheckOdd(Value)
    
    if(Ret == True):    
        print("It is Odd")
    else:
        print("It is Even")
    
if __name__ == "__main__":
    main()