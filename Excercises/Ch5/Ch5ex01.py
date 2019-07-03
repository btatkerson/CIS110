def main():
	day=int(input("Enter the day number: "))
	month=int(input("Enter the month number: "))
	year=int(input("Enter the year: "))
	months=["January","February","March","April"
		,"May","June","July","August","September"
		,"October","November","December"]
	monthStr=months[month-1]
	date1="{0}/{1}/{2}".format(month,day,year)
	date2="{0} {1},{2}".format(months[month-1],day,year)
	print("The date is {0} or {1}".format(date1,date2))
main()
