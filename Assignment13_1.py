# write a program which contains one function named as Area which accepts radius of circle from user and return its area. Default value of PI is 3.14
def Area(r):
    PI = 3.14
    area = PI * r * r
    print("Area of Circle is: ",area)

def main():
    
    print("Enter The Radius of Circle: ")
    r = float(input())
    
    Area(r)
    
if __name__ == "__main__":
    main()
    