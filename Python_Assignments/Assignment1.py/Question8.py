 ## Convert days into year and week into days.

Days =int(input("Enter days:"))
Week =int(input("Enter Week:"))
Remaining_days= int(input("Enter days:"))

year = Days // 365
Days = Week * 7
Remaining_days = Remaining_days % 365 

print('year', year)
print("Days", Days)
print("Remaining_days",Remaining_days)