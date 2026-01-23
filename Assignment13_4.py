# write a program which contains one function named as Binary which accepts one number from user and return its binary equivalent.
def main():
    num = int(input("Enter a number: "))
    
    binary = bin(num)
    print("Binary equivalent is:", binary[2:])

if __name__ == "__main__":
    main()
