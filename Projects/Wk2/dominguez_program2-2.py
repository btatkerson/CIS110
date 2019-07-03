'''
Program Name: dominguez_program2.py
Program Description: This program calculates the latency between NASA and The Curiosity Rover.
Author:Daniel Dominguez
Date Created:5/27/19
Notes of Interest:none
'''
import time


def main():
	#introduction
	print()
	print("This function estimates latency between NASA and The Curiosity Rover.")
	print("---------------------------------------------------------")
	#Stores the distance values in an array.
	distanceArray = [34000000,249000000,139000000]
	#create a literal to represent the speed of light
	speedOfLight = 186000

	#apply the algorythm to each element of the array and,
	#print the output to the screen.
	print("The time at Closest orbit is:", distanceArray[0]/speedOfLight,"seconds.")
	print("The time at Farthest orbit is:", distanceArray[1]/speedOfLight,"seconds.")
	print("The Average time is:", distanceArray[2]/speedOfLight,"seconds.")
main()

print("---------------------------------------------------------")
print("Press <Enter> to quit.")



print()
#prints authors name, class and date.
print("Daniel Dominguez")
print("CIS110 Program 2")
#Prints the current date and time using asctime()
print(time.asctime(time.localtime(time.time())))

