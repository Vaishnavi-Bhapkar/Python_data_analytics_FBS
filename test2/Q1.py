year = int(input("Enter a year:"))

if (year % 4):
    print("leap year")

elif (year % 100 ):
    print("Not a leap year")
    
else:
    (year % 400 )
    print("Leap year")


