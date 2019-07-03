import math
def sphereArea(radius):
	return 4*math.pi*radius**2

def sphereVolume(radius):
	return 4.0/3.0*math.pi*radius**3
gim
def main():
	print("This program computes the volume and surface area of a sphere.\n")
	
	r=float(input("Please enter the radius of the sphere:"))
	print("\nThe surface area is %0.2f square units." %(sphereArea(r)))
	print("The volume is a %0.2f cubic units." %(sphereVolume(r)))
main()
