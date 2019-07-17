'''
Program Name:dominguez_program8.py
Program Description:This program calculates and displays windspeed
Author:Daniel Dominguez
Date Created:7/17/19
Notes of Interest:wind chill = 35.74 + 0.6215T – 35.75(V0.16) + 0.4275T(V0.16)
'''
import math
import time
#Function to print the class signature
def classSignature():
	print("----------------------------------------")
	print("Daniel Dominguez")
	print("CIS110 Program 8")
	print(time.asctime(time.localtime(time.time())))

def windChill(t, v):
	if v<3:
		return("none")
	else:
		a=35.74+(0.6215*t)-35.75*pow(v,.16)+(0.4275*t)*pow(v,.16)
		return(math.ceil(a))

def main():
	temperatures=[ 60, 50, 40, 30, 20, 10,0, -10, -20]
	windSpeeds=5
	count=0
	print("\n")
	print("This program prints a formatted table of wind chill values.\n")
	print("====================Temperaratures_(F)==========================")
	print("w_mph|",str(temperatures).replace(","," | "))
	print("================================================================")
	for i in range(10):
		tempRow=[windSpeeds]
		for i in range(9):
			newValue=windChill(int(temperatures[count]),windSpeeds)
			tempRow.append(newValue)
			count=count+1
		print(" ",str(tempRow).replace(","," | "))
		print("________________________________________________________________")
		count=0
		windSpeeds=windSpeeds+5
	print("\n")
	classSignature()
main()
