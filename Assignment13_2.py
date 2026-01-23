# write a program which contains one function named as Area which accepts length and width of rectangle and return its area.
def main():
    length = float(input("Enter length of rectangle: "))
    width = float(input("Enter width of rectangle: "))

    area = length * width

    print("Area of rectangle is:", area)

if __name__ == "__main__":
    main()
