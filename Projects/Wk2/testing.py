###################################################################################################
#Program Name: dominguez_program2.py
#Program Description: This program calculates the latency between NASA and The Curiosity Rover.
#Author:Daniel Dominguez
#Date Created:5/27/19
#Notes of Interest:none
###################################################################################################
import time


def main():
	print()							#introduction
	print("This function estimates latency between NASA and The Curiosity Rover.")
	print("---------------------------------------------------------")

	distanceLabel = ["Closest","Farthest","Average"]	#Array of the labels for distances
	distanceArray = [34000000,249000000,139000000]		#Array of the distances 
	indexCounter = -1 					#Variable to represent the index value 										over two seperate arrays
	speedOfLight = 186000					#Variable to represetn the speed of light 										value.
	for i in distanceArray:					#Begins a for loop over the distance 										array.
		indexCounter = indexCounter+1 			#increases index counter by 1 each loop
		print("The time at",distanceLabel[indexCounter],"orbit is:", 
			distanceArray[indexCounter]/speedOfLight,"seconds.")	
								#Prints the output the screen for each 										element in the array.


main()								#Calls the main Function
print("---------------------------------------------------------")
print()
print("Daniel Dominguez")					#prints authors name, class and date.
print("CIS110 Program 2")
print(time.asctime(time.localtime(time.time())))		#Prints the current date and time using 								asctime()
input("Press <Enter> to quit.")
