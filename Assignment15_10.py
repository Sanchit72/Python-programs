#Write a lambda function using filter() which accepts a list of number and return the count of even number
Evencount = lambda Value : (Value % 2 == 0)

def main():
    
    L1 = list()
    print("Hwo many Element you want to store: ")
    No = int(input())
    
    for i in range(No):
        print("Enter ",i+1 ,"Number", end=' ')
        L1.append(int(input()))
        
    result = list(filter(Evencount , L1))
    print("Total Even:",len(result))
    
    
    
if __name__ == "__main__":
    main()