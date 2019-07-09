def isLeap(year):
    if year%4==0:
        return False
    elif year%100==0:
        if year%400==0:
            return True
        else:
            return False
    else:
        return True
def main():
    print("This program calculates whether a year i a leap year or not.\n")
    year=int(input("enter a year:"))

    if isLeap(year):
        print(year,"is a leap year.")
    else:
        print(year,"is not a leap year.")
main()
