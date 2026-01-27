#write a program which contains filter(),map(),and reduce()in it python application whcich contains one list of number list contains the number which are acceepted from user filter should filter out all prime number .map function will multiply each number by 2. reduce will retrun maximum number from that number(use normal function instead of lambda functi
# on) 

from functools import reduce


def CheckPrime(No):
    if No <= 1:
        return False
    for i in range(2, int(No**0.5) + 1):
        if No % i == 0:
            return False
    return True

def main():
    
    Data = []
    print("Enter Number of Element: ")
    No = int(input())
    
    for i in range(No):
        print("Enter Elemnt:",i+1)
        no = int(input())
        Data.append(no)
        
    print("Data is: ",Data) 
    
    FData = list(filter(lambda no : not CheckPrime(no),Data))
    print("Filtered Data is:",FData)
    
    MData = list(map(lambda no : no * 2,FData))
    print("Mapped Data is:",MData)
    
    RData = reduce(lambda no1,no2 : no1 if no1 > no2 else no2,MData)
    print("Reduced Data is:",RData)
    
if __name__ == "__main__":
    main()