def main():
	print("This program calculates the distance from a lightning strike.")
	print()
	
	seconds=int(input("Enter the number of seconds between the flash and crash:"))
	feet=1100*seconds
	miles=feet/5280.0


	print()	
	print("The lightning is approximatly", round(miles),"miles away.")

main()
