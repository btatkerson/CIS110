import math
def main():
	print("This program sums a series of numbers")
	print()
	#input
	n = int(input("How many numbers do you have?"))
	#processing
	total=0
	for i in range(n):
		num = float(input("Enter a number:"))
		total=total+num
	#output
	print()
	print("The sum of the number is:", total)
main()
