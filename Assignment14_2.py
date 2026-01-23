#  write a program which contains one lambda function which accepts one parameter and return its cube value.
Cube = lambda value : print("Cube is ",value * value * value)

def main():
    
    print("Enter The Number: ")
    No = int(input())
    
    Cube(No)
    
if __name__ == "__main__":
    main()