speedLimit=int(input("Please enter the speed limit: "))
clockedSpeed=int(input("Please enter the clocked speed: "))
fine=50
if clockedSpeed>speedLimit:
    fine=fine+((clockedSpeed-speedLimit)*5)
    if clockedSpeed>90:
        fine=fine+200
        print("Super Speeding", fine,"fine!")
    else:
        print("Speeding", fine,"fine!")

else:
    print("Not Speeding")
