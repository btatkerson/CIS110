'''
Program Name:CIS110 Program 1
Program Description: Print Hello World
Author:Daniel Dominguez
Date Created:5/21/19
Notes of Interest:none
'''
import time

def main():
    print("Hello World")

    
    #prints authors name, class and date.
    print("Daniel Dominguez")
    print("CIS110 Program 1")
    #Prints the current date and time using asctime()
    print(time.asctime(time.localtime(time.time())))
main()

