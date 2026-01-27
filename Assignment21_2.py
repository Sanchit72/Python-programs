#Design a python application that create two thread one thread display the maximum element and second thread display minimum elemnt from the same list this list should be accept from user.

import threading

def FindMax(Data):
    Max = max(Data)
    print("Maximum element is:", Max)
    
def FindMin(Data):
    Min = min(Data)
    print("Minimum element is:", Min)
    
def main():
    Data = []
    print("Enter Number of Elements: ")
    No = int(input())
    
    for i in range(No):
        print("Enter The Element:", i + 1)
        No = int(input())
        Data.append(No)
        
    print("Data is:", Data)
    
    threadMax = threading.Thread(target=FindMax, args=(Data,))
    threadMin = threading.Thread(target=FindMin, args=(Data,))
    
    threadMax.start()
    threadMin.start()
    
    threadMax.join()
    threadMin.join()