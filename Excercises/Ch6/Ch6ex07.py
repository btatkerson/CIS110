import math
from graphics import*
def fibo(n):
	curr,prev=1,1
	for i in range(n-2):
		cur,prev=curr+prev,curr
	return curr

def main():
	print("Nth Fibonacci number\n")
	n=int(input("Enter n:"))
	print("the Fibonacci value is",fibo(n))
main()
