'''
Program Name:dominguez_program6.py
Program Description:This program squares a list of numbers and returns the sum of the list and squared list
Author:Daniel Dominguez
Date Created:6/23/19
Notes of Interest:none
'''
import time
import random
import math
nums=[]
squaredList=[]
#Function to print the class signature
def classSignature():
	print("----------------------------------------")
	print("Daniel Dominguez")
	print("CIS110 Program 6")
	print(time.asctime(time.localtime(time.time())))

#Function to sum a list
def sumList(nums):
	sum=0
	for i in nums:
		sum=sum+i
	return sum

#Function to square a list of numbers
def squareEach(nums):
	for i in nums:
		squaredList.append(i*i)
	return squaredList
#Main Function 

def main():
	#Introduction and Input
	print("This program squares a list of numbers and returns the sum of the list and squared list\n")
	userNumbers=str(input("Enter number or numbers:"))

	#Splits the list of numbers by commas and appends to a list called "nums"
	for i in userNumbers.split(","):
		nums.append(int(i))

	print()#Original input and sum of the original input
	print("You entered: ",nums)
	print("The sum of the original list of numbers is: ", sumList(nums))
	print()#Squared input and sum of squared list.
	print("Your list squared is:",squareEach(nums))
	print("The sum of the squared list of numbers is: ", sumList(squaredList))
	classSignature()
main()
