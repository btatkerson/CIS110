'''
Program Name:dominguez_Program2.py
Program Description:This program accepts two inputs as base and exponant and returns the answer as an int.
Author:Daniel Dominguez
Date Created:6/2/19
Notes of Interest:none
'''
import time
import math
def main():
    #Prompts the user for two numbers.
    print("-------------------------------------------")
    base = eval(input("Please enter the Base: "))
    expon = eval(input("Please enter the Exponent: "))
    
    #Processes the users input usig the math::pow() function and stores the value in answer variable.
    answer = pow(int(base),int(expon))
    
    #Outputs the results of the power to the user as an int.
    print(base,"to the power of ",expon,"is: ",answer)
    print("-------------------------------------------")
    input("Press <ENTER> to quit.")

    #prints authors name, class and date.
    print("Daniel Dominguez")
    print("CIS110 Program 3")
    #Prints the current date and time using asctime()
    print(time.asctime(time.localtime(time.time())))
main()

