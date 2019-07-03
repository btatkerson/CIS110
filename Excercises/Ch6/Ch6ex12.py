import math
from graphics import*
def sumList(nums):
	total=0
	for n in nums:
		total=total+n
	return total

def main():
	nums=list(range(15))
	print(sumList(nums))
main()
