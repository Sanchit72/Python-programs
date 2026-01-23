# write a lambda function using filter() which accept a list of number and return a list of even number
def checkeven(No):
    return (No % 2 == 0)

def main():
    
    Data = [12,34,21,44,22,55,32,7,17,13,]
    print("Actual Data: ",Data)
    
    FData = list(filter(checkeven, Data))
    print("Data After Filter is:",FData)
    
    
    
if __name__ == "__main__":
    main()