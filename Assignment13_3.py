# write a program which contains one function named as Perfect which accepts one number from user and print whether that number is perfect or not.

def Perfect(value):
    sum = 0
    for i in range(1, value):
        if value % i == 0:
            sum += i
    if sum == value:
        print(f"{value} is a Perfect Number")
    else:
        print(f"{value} is not a Perfect Number")

def main():
    
    print("Enter The Number: ")
    No = int(input())
    
    Perfect(No)
    
if __name__ == "__main__":
    main()