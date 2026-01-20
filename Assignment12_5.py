def reverse(value):
    for i in range(value,0,-1):
        print(i)
def main():
   
   print("Enter The Number: ")
   No = int(input())
   
   reverse(No)
   
if __name__ == "__main__": 
    main()