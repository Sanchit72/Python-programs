# write a program which contain filter(),map() and reduce() in it.python application one list of number list contains number which are accept from user filter should filter out all such number which greater than or equal to 70 and less than or equl to 90 map function will increase each number by 10 reduce will return product of all that number.
from functools import reduce



def main():

    Data = []
    print("Enter number of elements:")
    size = int(input())

    for i in range(size):
        print("Enter element:",i+1)
        no = int(input())
        Data.append(no)

    print("Data is:",Data)

    FData = list(filter(lambda no : (no >= 70) and (no <= 90),Data))
    print("Filtered data is:",FData)

    MData = list(map(lambda no : no + 10,FData))
    print("Mapped data is:",MData)

    RData = reduce(lambda no1,no2 : no1 * no2,MData)
    print("Reduced data is:",RData)
    
if __name__ == "__main__":
    main()