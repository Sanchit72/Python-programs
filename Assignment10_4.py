#write a program which contains one function named as Even. That function should accept one number from user and print even numbers upto that number.

def Even(No):
    for i in range(1,No+1):
        if(i % 2 == 0):
            print(i)
            

    
def main():
    
    print("Entr The number:")
    No = int(input())
    
    Even(No)
    
if __name__ == "__main__":
    main()
    