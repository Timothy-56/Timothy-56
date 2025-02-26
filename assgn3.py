import math

def area_triangle(base, height):
    return 0.5 * base * height

def area_rectangle(length, width):
    return length * width

def area_circle(radius):
    return math.pi * radius * radius

def perimeter_triangle(a, b, c):
    return a + b + c

def perimeter_rectangle(length, width):
    return 2 * (length + width)

def circumference_circle(radius):
    return 2 * math.pi * radius

def main():
    while True:
        print("Choose the shape:")
        print("1. Triangle (Area only with base and height)")
        print("2. Triangle (Perimeter with three sides)")
        print("3. Rectangle")
        print("4. Circle")
        
        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            print("Area of triangle:", area_triangle(base, height))
            input("Press Enter to proceed to the next calculation...")
        elif choice == 2:
            a = float(input("Enter the first side of the triangle: "))
            b = float(input("Enter the second side of the triangle: "))
            c = float(input("Enter the third side of the triangle: "))
            print("Perimeter of triangle:", perimeter_triangle(a, b, c))
            input("Press Enter to proceed to the next calculation...")
        elif choice == 3:
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            print("Area of rectangle:", area_rectangle(length, width))
            print("Perimeter of rectangle:", perimeter_rectangle(length, width))
            input("Press Enter to proceed to the next calculation...")
        elif choice == 4:
            radius = float(input("Enter the radius of the circle: "))
            print("Area of circle:", area_circle(radius))
            print("Circumference of circle:", circumference_circle(radius))
            input("Press Enter to proceed to the next calculation...")
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()

    
      

