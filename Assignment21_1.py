# Design a python application that create two threads named prime and nonprime accept list of intger priem display all prime number and nonprime thread dispaly all non-prime number
import threading
def Prime(No):
    pass

def main():
    
    Data = []
    print("Enter Number of Elemnt: ")
    No = int(input())
    
    for i in range(No):
        print("Enter The Elemnt:",i+1)
        No=int(input())
        Data.append(No)
        
    print("Data is:",Data)
    
    Fdata = threading.Thread(target=Prime,args=No)  
    print("Prime is ",Fdata)    
    
if __name__ =="__main__":
    main()  