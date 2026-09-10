## Write a program to input electricity unit charges and calculate total electricity billaccording to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill.....


unit = int(input("Enter units:"))

if (unit <= 50):
        Bill = (unit * 0.50)

elif (unit <= 150):
    Bill = 50 * 0.50 + ((unit - 50) * 0.75)

elif (unit <= 250 ):
     Bill = 50 * 0.50 +  100 * 0.75 + ((unit - 150) * 1.20)

else:
     (unit > 250)
     Bill = 50 * 0.50 + 100 * 0.75 + 100 * 1.20 + ((unit - 250) * 1.50)

surcharge = Bill * 0.20

total_electricity_bill = Bill + surcharge 

print("total_electricity_bill:", total_electricity_bill)









