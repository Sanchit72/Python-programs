# Write a lambda function using reduce() which accept a list of number and return the product of al element
from functools import reduce

Product = lambda value1, value2: value1 * value2
def main():

    Data = [12,3,5,6,7,3,8]
    print("Actual Data is: ",Data)
    
    FData = reduce(Product,Data)
    print("After Reduce Data: ",FData)

if __name__ == "__main__":
    main()