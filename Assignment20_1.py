# Design a python application two seprate thread named even and odd 1.The even thread should display first 10 even number and odd thread dispaly first 10 odd number.

import threading

def Even(No):
    for i in range(1,No+1):
        if(i%2==0):
            print("Even number:",i)
    
def Odd(No):
    for i in range(1,No+1):
        if(i%2!=0):
            print("Odd number:",i)
    
def main():
    
    list = []
    print("Enter number:")
    No = int(input())
    
    t1 = threading.Thread(target=Even,args=(No,))
    t2 = threading.Thread(target=Odd,args=(No,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == "__name__":
    main()
    