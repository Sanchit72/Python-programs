def Factors(value):
    for i in range(value+1):
        if i != 0 and value % i == 0:
            print(i)

def main():
    
    print("Enter The Number: ")
    No = int(input())
    
    Factors(No)
    
if __name__ == "__main__":
    main()