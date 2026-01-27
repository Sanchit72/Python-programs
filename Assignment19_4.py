# wirte a program which contains filter(),map() and reduce() in it .python application which contains one list of number list contains the number which are accept from user. filter should filter out all such number which are even map function will calculate its square reduce will return addition of all that number.
from functools import reduce


def main():
    
    Data = []
    print("Enter Number of Element: ")
    No = int(input())
    
    for i in range(No):
        print("Enter Elemnt:",i+1)
        no = int(input())
        Data.append(no)
        
    print("Data is: ",Data) 
    
    FData = list(filter(lambda no : no % 2 == 0,Data))
    print("Filtered Data is:",FData)
    
    MData = list(map(lambda no : no * no,FData))
    print("Mapped Data is:",MData)
    
    RData = reduce(lambda no1,no2 : no1 + no2,MData)
    print("Reduced Data is:",RData)
    
    
if __name__ == "__main__":
    main()