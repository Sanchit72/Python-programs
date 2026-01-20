def Vowel(ch):
    if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or
        ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
        print(f"{ch} is Vowel")
    else:
        print(f"{ch} is Not Vowel")

def main():
    
    print("Enter The Charecter:")
    ch = input()
    
    Vowel(ch)
if __name__ =="__main__":
    main()