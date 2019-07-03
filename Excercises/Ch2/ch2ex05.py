def main():
    print("This program converts temperature from Celsius to farenheit.")
    print()
    print("Celsius Fahrenheit")
    print("------------------")
    print("0             32.0")
    for  celsius in [10,20,30,40,50,60,70,80,90]:
        fahrenheit=9/5*celsius+32
        print(celsius,"          ",fahrenheit)

    print("100           212.0")
    input("Press the <Enter> key to quit.")
main()
