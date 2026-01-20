def Multiplication(Value):
    for i in range(1,11):
        print(Value * i)
        

def main():
    
    print("Enter The Number: ")
    No = int(input())
    result = 0
    
    Multiplication(No)
    
    
if __name__ == "__main__":
    main()