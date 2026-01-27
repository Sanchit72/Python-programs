# write a program which accept N number from user and store it into list. return minimum of all elements from that list.

def Minimum(List):
    Min = List[0]
    for i in range(1, len(List)):
        if List[i] < Min:
            Min = List[i]
    return Min
def main():
    
    List = []
    No = int(input("Enter The Number of elemnt: "))
    for i in range(No):
        Value = int(input("Enter element {}: ".format(i+1)))
        List.append(Value)

    Ret = Minimum(List)
    print("Minimum number from list is:", Ret)
    
if __name__ == "__main__":
    main()