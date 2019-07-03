import math
#input
print("This program calculates the surface area and volume of a sphere!")
print()
#processing
radius=float(input("Please enter the radius of the sphere: "))
volume=4/3*math.pi*radius**3
area=4*math.pi*radius**2
#output
print("The volume is", volume, "cubic units.")
print("The surface area is", area,"square units.")
