# Write a lambda function using map() which accept list of number and returns a list of square of each number.
def Square(No):
    return No * No

def main():
    
    Data = [12,32,43,43,54,24,56,23,15]
    print("Actual data is",Data)
    
    FData = list(map(Square, Data))
    print("Data After Maping is: ",FData)
    
if __name__ == "__main__":
    main()
    