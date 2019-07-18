def main():
    print("Number of years for an investment to double.\n")
    apr=float(input("What is the annual interest rate?"))
    principal=float(input("What is the initial investment?"))
    years=0
    goal=principal*2
    while principal<goal:
        principal=principal*(1+apr)
        years=years+1
    print("Years to double:",years)
main()
