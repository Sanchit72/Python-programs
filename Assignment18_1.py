# write a program which accept N number from user and store it into list. return addition of all elements from that list.
def Sum(List):
    Sum = 0
    for i in range(len(List)):
        Sum = Sum + List[i]
    return Sum

def main():
    
    List = []
    No = int(input("Enter The Number of elemnt: "))
    for i in range(No):
        Value = int(input("Enter element {}: ".format(i+1)))
        List.append(Value)

    Ret = Sum(List)
    print("Addition of all elements is:", Ret)
    
if __name__ == "__main__":
    main()