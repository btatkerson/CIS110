import math
def main():
	print("This  program calculates the length of a ladder required, given the height and angle.")
	print()
	#input
	height=float(input("How high must you reach?"))
	angle=float(input("What will the ladder angle be (in degrees)?"))
	#processing
	radians=math.radians(angle)
	length=height/math.sin(radians)
	#output
	print()
	print("Length of ladder required:", length)
main()
