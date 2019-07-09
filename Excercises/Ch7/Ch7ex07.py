def main():
    print("Babysitting calc\n")
    print("Enter times use 24 hour format(e.g 8pm is 20:00)")
    sHours,sMin=input("Starting time (HH:MM): ").split(":")
    eHours,eMin=input("Ending time (HH:MM): ").split(":")

    start=int(sHours)+float(sMin)/60.0
    end=int(eHours)+float(eMin)/60.0

    if end<start:
        end=end+24

    bedtime=21.0

    if start<bedtime:
        if end <bedtime:
            primeHours=end-start
            extraHours=0.0
        else:
            primeHours=bedtime-start
            extraHours=end-bedtime
    else:
        primeHours=0.0
        extraHours=end-start
    pay=2.50*primeHours+1.75*extraHours
    print("The total payment due: ${0:0.2f}".format(pay))
main()
