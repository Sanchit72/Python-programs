
def Addition(No1,No2):
    Ans = No1+No2
    return Ans

def substraction(No1,No2):
    Ans = No1-No2
    return Ans

def Multiplcation(No1,No2):
    Ans = No1*No2
    return Ans

def Devision(No1,No2):
    Ans = No1/No2
    return Ans

def main():
    print("Enter first number:")
    Value1 = int(input())

    print("Enter second number:")
    Value2 = int(input())

    Ret = Addition(Value1,Value2)

    print("Addition is:",Ret)
    
    Ret = substraction(Value1,Value2)

    print("substraction is:",Ret)
    
    Ret = Multiplcation(Value1,Value2)

    print("Multiplcation is:",Ret)
    
    Ret = Devision(Value1,Value2)

    print("Devision is:",Ret)
main()