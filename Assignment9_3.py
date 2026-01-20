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