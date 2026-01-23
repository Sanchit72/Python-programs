#write a program which contains one function named as Cube.

def Cube(value1):
    ans = 0
    
    ans = value1**3
    
    return ans
    


def main():
    
    print("Enter The Number: ")
    No1 = int(input())
    
    ret= 0
    
    ret = Cube(No1)
    
    print("Cube is :",ret)
    
if __name__ == "__main__":
    main()