def main():
    num = int(input("Enter a number: "))
    
    binary = bin(num)
    print("Binary equivalent is:", binary[2:])

if __name__ == "__main__":
    main()
