# Dsipaly pattern
# 1    2   3   4
# 1    2   3   4
# 1    2   3   4
# 1    2   3   4

def Pattern(No1,No2):
    
    for i in range(No1):
        for j in range(1, No2 + 1):
            print(j, end="\t")
        print()
        
def main():
    
    No1 = int(input("Enter Number: "))
    No2 = int(input("Enter Number: "))
    
    Pattern(No1,No2)
    
if __name__ == "__main__":
    main()