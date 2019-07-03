import math

def main():
	print("This program calculates the cost per square inch of a circular pizza!")
	print()

	diam=float(input("Please enter the Diameter of a pizza (in inches):"))
	price=int(input("Please enter the price of the pizza (in cents):")
	area = math.pi*(diam/2)**2
	cost = price/area
	print()
	print("The cost is", cost,"cents per square inch.")
main()
