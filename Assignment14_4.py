# write a program which contains one lambda function which accepts two parameters and return its maximum value.

Minimum = lambda value1,value2:print("Minimum is ",min(value1,value2))

def main():
    
    ret = False
    print("Enter The Number: ")
    No1 = int(input())
    
    print("Enter Second Number: ")
    No2 = int(input())
    
    Minimum(No1,No2)
    
if __name__ == "__main__":
    main()