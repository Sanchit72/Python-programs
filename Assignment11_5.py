def pailndrome(No):
    rev = 0
    temp = No
    while(No != 0):
        digit = No % 10
        rev = rev * 10 + digit
        No = No // 10
    if(temp == rev):
        print(f"{temp} is a palindrome number")
    else:
        print(f"{temp} is not a palindrome number")
def main():
    
    print("Enter The Number:")
    Value = int(input())
    
    pailndrome(Value)
    
if __name__ == "__main__":
    main()