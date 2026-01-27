# Display Pattern
#  *    *   *   *
#  *    *   *   
#  *    *   
#  *    
def Pattern(No1,No2):
    for i in range(No1,0,-1):
        for j in range(i):
            print("i",end="\t")
        print()
        
def main():
    
    No1 = int(input("Enter Number: "))
    No2 = int(input("Enter Number: "))
    
    Pattern(No1,No2)
    
if __name__ == "__main__":
    main()