'''
Program Name:dominguez_program5.py
Program Description:This encrypts a message using a substition cypher(caesar)
Author:Daniel Dominguez
Date Created:5/21/19
Notes of Interest:none
'''
import time

def main():
	#variables
	print("This program uses a basic Substitution Cypher to encrypt a message.")
	message=input("Please enter the message to encode: ")
	key=int(input("Enter Key Value: "))
	codedMessage=[]
	decodedMessage=[]

	#encoding
	for i in message:
		codedChar=int(ord(i))+key
		codedMessage.append(chr(codedChar))
	print("-------------------------------------------")
	print("This is your encrypted message")
	print("".join(codedMessage))
	
	#decoding 
	print("-------------------------------------------")
	print("This is your decrypted message")
	for n in codedMessage:
		decodedChar=chr(int(ord(n))-key)		
		decodedMessage.append(decodedChar)
	print("".join(decodedMessage))
	print("-------------------------------------------")
	print("")

	#prints authors name, class and date.
	print("Daniel Dominguez")
	print("CIS110 Program 5")
	#Prints the current date and time using asctime()
	print(time.asctime(time.localtime(time.time())))
main()
 
