def Divisible(value):
    if(value % 5 ==0):
        print(True)
    else:
        print(False)
def main():
    bret =False
    No = int(input("Enter The Number: "))
    
    Divisible(No)
    
    

if __name__ == "__main__":
    main()