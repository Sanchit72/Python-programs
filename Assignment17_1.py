#Write a program  which contains 4 function  Add() for addition Sub(), Mult(), Div() accept two number and perform the operation
def Add(Value1,Value2):
    Ans = 0
    Ans = Value1 + Value2
    return Ans
def Sub(Value1,Value2):
    Ans = 0
    Ans = Value1 - Value2
    return Ans

def Mult(Value1,Value2):
    Ans = 0
    Ans = Value1 * Value2
    return Ans

def Div(Value1,Value2):
    Ans = 0
    Ans = Value1 / Value2
    return Ans

def main():
    
    No1 = int(input("Enter First Number: "))
    No2 = int(input("Enter Second Number: "))
    Ret = 0
    Ret = Add(No1,No2)
    print("Addition is: ",Ret)
    
    Ret = Sub(No1,No2)
    print("Substraction is: ",Ret)
    
    Ret = Mult(No1,No2)
    print("Multiplication is: ",Ret)
    
    Ret = Div(No1,No2)
    print("Division is: ",Ret)

if __name__ == "__main__":
    main()