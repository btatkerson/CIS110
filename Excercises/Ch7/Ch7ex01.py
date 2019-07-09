totalHours=int(input("How many hours did you work this week? "))
hourlyWage=int(input("How much do you make per hour?"))
compensation=0
overtimeHours=0
if totalHours>40:
    overtimeHours=totalHours-40 #Store the excess hours in variable
    compensation=hourlyWage*40 #Store max base pay in variable
    otPay=overtimeHours*(hourlyWage+(hourlyWage*.5))
    print("Compensation: ",compensation+otPay)
else:
    compensation=hourlyWage*totalHours
    print("Compensation: ",compensation)
