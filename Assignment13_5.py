# write a program which contains one function named as Marks which accepts marks from user and display the class of student.

def marks(value):
    if(value>75):
        print("Distinction")
    elif(value>60):
        print("First Class")
    elif(value>50):
        print("Second Class")
    elif(value<50):
        print("Fail")
def main():
    
    print("Enter The Number:")
    No = int(input())
    
    marks(No)
    
if __name__ =="__main__":
    main()