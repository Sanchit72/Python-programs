#write a program which contains one function named as Square.# That function should accept one number from user and return its square.# Input : 4 # Output : 16

def Square(value1):
    ans = 0
    
    ans = value1*value1
    
    return ans
    


def main():
    
    print("Enter The Number: ")
    No1 = int(input())
    
    ret= 0
    
    ret = Square(No1)
    
    print("Square is :",ret)
    
if __name__ == "__main__":
    main()