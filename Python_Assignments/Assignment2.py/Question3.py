##  Convert Distant feet and inches  into meter and centimeter 

Feet = int(input("Enter Feet:"))
Inches=int(input("Enter Inches:"))


total_meters = ((Feet * 12) + Inches) * 0.0254

meters = int(total_meters)
centimeters = round((total_meters - meters) * 100, 2)

print(F"{meters}m ")
print(F"{centimeters}cm")

