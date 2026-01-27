#Write a Program which accept one number and dispaly pattern
#  *    *   *   *
#  *    *   *   *
#  *    *   *   *
#  *    *   *   *

def Pattern(No1,No2):
    
    for i in range(No1):
        for j in range(No2):
            print("*",end="\t")
        print()
    
def main():
    
    No1 = int(input("Enter Number: "))
    No2 = int(input("Enter Number: "))
    
    Pattern(No1,No2)
    
if __name__ == "__main__":
    main()