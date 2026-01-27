# write a program which accept N number from user and store it into list Return Maximum number from list

def Maximum(List):
    Max = List[0]
    for i in range(1, len(List)):
        if List[i] > Max:
            Max = List[i]
    return Max
def main():
    
    List = []
    No = int(input("Enter The Number of elemnt: "))
    for i in range(No):
        Value = int(input("Enter element {}: ".format(i+1)))
        List.append(Value)

    Ret = Maximum(List)
    print("Maximum number from list is:", Ret)
    
if __name__ == "__main__":
    main()