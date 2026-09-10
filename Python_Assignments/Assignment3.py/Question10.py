# Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)....

gender =input("Enter gender :")
age = int(input("Enter age :"))
if (gender == "female"):
   if (age >= 18): 
    print("Eligible for married")

   else:
        print("Not eligible")

if (gender == "male"): 
    if (age >=21):
     print("Eligible for married")

    else:
        print("Not eligible")
    





