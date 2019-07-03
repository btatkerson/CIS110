def main():
    print("This program calculates the future value of an investment.")
    print()

    principal=eval(input("Enter the initial principal: "))
    apr=eval(input("Enter the annual interest rate(APR): "))
    years=eval(input("How many years are you investing? "))
   
    for i in range(years):
        principal=principal*(1+apr)
    print("The amount in ",years,"year investment is: ",principal)
    print("Press <Enter> to quit.")
main()
