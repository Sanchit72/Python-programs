#write a program which contains one function named as Reverse. That function should accept one number from user and print that number in reverse order.
def reverse(value):
    for i in range(value,0,-1):
        print(i)
def main():
   
   print("Enter The Number: ")
   No = int(input())
   
   reverse(No)
   
if __name__ == "__main__": 
    main()