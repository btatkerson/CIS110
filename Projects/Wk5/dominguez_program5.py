'''
Program Name:dominguez_program5.py
Program Description:This encrypts a message using a substition cypher(caesar)
Author:Daniel Dominguez
Date Created:6/21/19
Notes of Interest: This one was fun! 
'''
import time
def main():
	print("This program uses a basic (Ceasar)Substitution Cypher to encrypt a message.")
	message=input("Please enter the message to encode: ")				
	key=int(input("Enter Key Value: "))
	message=message.lower()
	codedMessage=[]
	decodedMessage=[]
	lowCap=96
	maxCap=122
							#Encoding Starts Here 
	for i in message:					
		codedChar=ord(i)+key
							#Check to see if the new encoded char is out of range
		if ord(i)+key>maxCap:
							#If the character ordinance is out of range, subtract the max value from it and then add it to the minimum value
			codedMessage.append(chr((codedChar-maxCap)+lowCap))
		else:	
							#otherwise just store the value with the key applied 		
			codedMessage.append(chr(int(codedChar)))
							#Decoding Starts Here
	for n in codedMessage:
							#If the ordinance-key-lowcap is less than or equal to 0 or the low cap (a)		
		if (int(ord(n))-key)-lowCap<=0 and chr(int(ord(n))-key)!=lowCap:
							#treat this as a special case	
			decodedMessage.append(chr((((int(ord(n))-key)-lowCap)+maxCap))) 
		else:
							#otherwise apply regular decryption algorithm
			decodedMessage.append(chr(int(ord(n))-key))
							#join the list together and "update" variable
	decodedMessage="".join(decodedMessage)
	print("-----------------------------------------------------")
	print("Encrypted string: ","".join(codedMessage))
							#Print the decoded message, and repalce : from encryption with spaces
	print("Unencrypted string: ",decodedMessage.replace(":"," "))
	print("-----------------------------------------------------")
	print("Daniel Dominguez")			#prints authors name, class and date.
	print("CIS110 Program 5")			#Prints the current date and time using asctime()
	print(time.asctime(time.localtime(time.time())))
main()
