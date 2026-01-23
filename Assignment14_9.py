   
Multiplication = lambda No1,No2,No3 : print("Largest is",max(No1,No2,No3))
       
def main():
    Value = 0
    Ret = 0
    
    print("Enter Number:")
    Value1 = int(input())
    
    print("Enter Number:")
    Value2 = int(input())
    
    print("Enter Number:")
    Value3 = int(input())
    
    Ret = Multiplication(Value1,Value2,Value3)
    
if __name__ == "__main__":
    main()