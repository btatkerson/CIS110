def main():
	print("This program converts temperature from Celsius to farenheit.")
	print()
	for i in range(5):
		celsius=eval(input("What is the temperature in Celsius? "))
		farenheit=9/5*celsius+32
		print("The Temperature in farenheit is: ",farenheit)
		print()

	input("Press the <Enter> key to quit.")

main()
