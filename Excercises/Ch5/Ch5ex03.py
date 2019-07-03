def main():
	print("This program accepts a exam score and a grade/n")
	userValue=int(input("Enter a score betwen 0-100:"))
	grades=["F","F","F","F","F","F","D","C","B","A","A"]
	index=int(userValue)//10
	final=grades[int(index)]
	print("The grade is: ",final)
main()
