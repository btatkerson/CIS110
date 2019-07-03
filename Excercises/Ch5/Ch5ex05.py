def main():
	print("This program computes the numerical value of a single name/n")
	nameString=input("Enter a name: ")
	total=0
	for l in nameString:
		total=total+ord(l.lower())-ord('a')+1
	print("The value for ",nameString,"is ",total)
main()
