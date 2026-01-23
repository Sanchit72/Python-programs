#write a program which contains four functions as Addition, Substraction, Multiplication, Division. All functions accepts two parameters as number and perform the operation.
def Addition(value1,value2):
    print("Addition is" ,value1+value2)
    
def Substraction(value1,value2):
    print("Substraction is: ",value1-value2)
    

def Multiplication(value1,value2):
    print("Multiplication is: ",value1*value2)
    
def Division(value1, value2):
    print("Division is: ",value1 / value2)
    
def main():

    print("Enter First Number: ")
    No1  = int(input())
    
    print("Enter Second Number: ")
    No2 = int(input())
    
    Addition(No1,No2)
    Substraction(No1,No2)
    Multiplication(No1,No2)
    Division(No1,No2)

if __name__ =="__main__":
    main()