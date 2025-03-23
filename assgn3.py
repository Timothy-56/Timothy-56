import math

# Function to calculate the area of a triangle
def area_triangle(base, height):
    return 0.5 * base * height  # Formula: 0.5 * base * height

# Function to calculate the area of a rectangle
def area_rectangle(length, width):
    return length * width  # Formula: length * width

# Function to calculate the area of a circle
def area_circle(radius):
    return math.pi * radius ** 2  # Formula: π * radius^2

# Function to calculate the perimeter of a triangle
def perimeter_triangle(a, b, c):
    return a + b + c  # Sum of all sides

# Function to calculate the perimeter of a rectangle
def perimeter_rectangle(length, width):
    return 2 * (length + width)  # Formula: 2 * (length + width)

# Function to calculate the circumference of a circle
def circumference_circle(radius):
    return 2 * math.pi * radius  # Formula: 2 * π * radius

# Main function to interact with the user
def main():
    while True:
        print("\nChoose the shape:")
        print("1. Triangle (Area using base and height)")
        print("2. Triangle (Perimeter using three sides)")
        print("3. Rectangle (Area and Perimeter)")
        print("4. Circle (Area and Circumference)")
        print("5. Exit")  # Option to exit the program

        # Get user choice
        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            # Calculate area of triangle
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            print("Area of the triangle:", area_triangle(base, height))
        elif choice == 2:
            # Calculate perimeter of triangle
            a = float(input("Enter the first side of the triangle: "))
            b = float(input("Enter the second side of the triangle: "))
            c = float(input("Enter the third side of the triangle: "))
            print("Perimeter of the triangle:", perimeter_triangle(a, b, c))
        elif choice == 3:
            # Calculate area and perimeter of rectangle
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            print("Area of the rectangle:", area_rectangle(length, width))
            print("Perimeter of the rectangle:", perimeter_rectangle(length, width))
        elif choice == 4:
            # Calculate area and circumference of circle
            radius = float(input("Enter the radius of the circle: "))
            print("Area of the circle:", area_circle(radius))
            print("Circumference of the circle:", circumference_circle(radius))
        elif choice == 5:
            # Exit the program
            print("Exiting the program. Goodbye!")
            break
        else:
            # Handle invalid input
            print("Invalid choice. Please choose a valid option.")

# Entry point of the program
if __name__ == "__main__":
    main()

    
      

