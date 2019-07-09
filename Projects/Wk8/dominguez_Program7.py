'''
Program Name:dominguez_program7.py
Program Description:This program calculates easter in a gaven year within the range of 1900-2099.
Author:Daniel Dominguez
Date Created:7/9/19
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
	print("CIS110 Program 7")
	print(time.asctime(time.localtime(time.time())))

def main():
    print("This program calculates easter in a given year.\n")
    year=int(input("Please enter a year between the range of 1900-2099:\n"))
    month=""
    if year>2099 or year<1900:
        print("This year is out of range.")
        classSignature()
    else:
        a=year%19
        b=year%4
        c=year%7
        d=(19*a+24)%30
        e=(2*b+4*c+6*d+5)%7

        if 22+d+e>31:
            day=(22+d+e)-31
            month=month+"April"
            print("Easter in",year,"is on",month,day)
            classSignature()
        else:
            day=(22+d+e)
            month=month+"March"
            print("Easter in",year,"is on",month,day)
            classSignature()
main()
