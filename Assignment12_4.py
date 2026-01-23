#write a program which contains one function named as Number. That function should accept one number from user and print that number of even numbers on screen.
def Number(value):
    for i in range(1,value+1):
        print(i)
def main():
   
   print("Enter The Number: ")
   No = int(input())
   
   Number(No)
   
if __name__ == "__main__": 
    main()