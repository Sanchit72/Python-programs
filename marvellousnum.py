# marvellousnum.py
def chkprime(No):
    if No <= 1:
        return False
    for i in range(2, int(No**0.5) + 1):
        if No % i == 0:
            return False
    return True
def listprime(List):
    Sum = 0
    for num in List:
        if chkprime(num):
            Sum += num
    return Sum