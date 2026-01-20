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
    