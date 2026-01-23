# Write a lambda function using reduce() which accept list of number and return the minimum elemnt
from functools import reduce
min = lambda No1 , No2:No1 if No1 < No2 else No2

def main():
    
    Data = [23,43,23,54,23,12,22,15,14,20]
    print("Actual Data is: ",Data)
    
    FData = reduce(min , Data)
    print("Data After Reduce is: ",FData)
    
if __name__ == "__main__":
    main()