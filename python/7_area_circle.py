import math
def calculate_circle_area(rad):
    # return math.pi * (rad**2) 
    return 3.14 * (rad**2) 

radius = float(input("Enter the Radius of the Circle: "))
print("The Area of the Circle is:", calculate_circle_area(radius))