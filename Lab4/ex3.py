import math

# function to calculate the area of a circle
def circle_area(radius):
    return math.pi * radius**2

# example usage
radius = int(input("Enter the radius of the circle: "))
area = circle_area(radius)
print(f"The area of the circle with radius {radius} is {area}")
