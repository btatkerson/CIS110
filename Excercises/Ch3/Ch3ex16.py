import math
def main():
	print("This program sums a series of numbers")
	print()
	#input
	n = int(input("Enter the value of n:"))
	#processing
	Curr, prev =1,1
	for i in range(n-2):
		Curr,prev=Curr+prev,Curr
	#output
	print()
	print("The nth Fibonacci number is:", Curr)
main()
