# Write a lambda function using reduce() which accept a list of number and return the addition of all element
from functools import reduce
def Add(No1,No2):
    return No1 + No2

def main():
    
    Data = [12,33,43,21,10,14,13,30,20]
    print("Actual Data: ",Data)
    
    FData = reduce(Add , Data)
    print("Data After Reduce is: ",FData)
    
if __name__ == "__main__":
    main()