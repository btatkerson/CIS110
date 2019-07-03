def main():
    print("This program calculates the future value of a yearly investment.")
    print()

    payment=eval(input("Enter the amount to invest each year: "))
    apr=eval(input("Enter the annual interest rate(APR): "))
    years=eval(input("How many years are you investing? "))
   
    principal=0.0
    for i in range(years):
        principal=(principal+payment)*(1+apr)
    print("The amount in ",years,"years is: ",principal)
    print("Press <Enter> to quit.")
main()
