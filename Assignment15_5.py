# Write a lambda function using reduce() which accept a list of number and return the Maximum number
from functools import reduce
Max = lambda No1,No2:No1 if No1 > No2 else No2
def main():
    
    Data = [12,33,43,21,10,14,13,30,20]
    print("Actual Data: ",Data)
    
    FData = reduce(Max , Data)
    print("Data After Reduce is: ",FData)
    
if __name__ == "__main__":
    main()