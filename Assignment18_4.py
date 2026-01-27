# write a program which accept n number from user and store it into list accept one another number from user return frequency of that number from list.

def Frequency(List, No):
    Count = 0
    for i in range(len(List)):
        if List[i] == No:
            Count = Count + 1
    return Count

def main():

    List = []
    N = int(input("Enter The Number of elemnt: "))
    for i in range(N):
        Value = int(input("Enter element {}: ".format(i+1)))
        List.append(Value)

    No = int(input("Enter number to find frequency: "))
    Ret = Frequency(List, No)
    print("Frequency of {} in list is: {}".format(No, Ret))
    
if __name__ == "__main__":
    main()