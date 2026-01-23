#Write a lambda function using filter() which accept a list of number divisible by both 3 and 5
Divisible = lambda Value : (Value % 3 == 0 and Value % 5 ==0)

def main():
    
    Data = [23,12,15,24,18,5,3,8]
    print("Actual Data is: ",Data)
    
    
    FData = list(filter(Divisible , Data))
    print("After Filter Data: ",FData)
    
if __name__ == "__main__":
    main()