def Check(Value):
    if(Value > 0):
        print("Positive")
    else:
        print("Negative")
def main():
    
    print("Enter The Number: ")
    No = int(input())
    
    Check(No)
    
if __name__ == "__main__":
    main()
    