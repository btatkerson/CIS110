def main():
	print("This program builds acronyms/n")
	p=input("Enter a phrase: ")
	a=""
	for w in p.split():
		a=a+w[0]
	a=a.upper()
	print("For the phrase",p," the acronym is: ",a)	
main()
