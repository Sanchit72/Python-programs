# Write a program whcih accept n number from user and store it into list. return addition of all prime number from that list. main python file accept n number from user and pass each number to chkprime() function which is part of our user defined module named as marvellousnum.name of the function from main python file should be listprime()

from marvellousnum import listprime

def main():
    List = []
    No = int(input("Enter The Number of elemnt: "))
    for i in range(No):
        Value = int(input("Enter element {}: ".format(i+1)))
        List.append(Value)

    Ret = listprime(List)
    print("Addition of all prime numbers is:", Ret)
    
if __name__ == "__main__":
    main()