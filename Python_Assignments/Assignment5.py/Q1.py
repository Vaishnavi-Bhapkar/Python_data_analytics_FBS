# Write a program to prompt user to enter userid and password. If Id and password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate....

id = 1234
password = "admin"

for i in range (3):

    id = int(input("Enter id:"))
    password = (input("Enter password:"))

    if id == 1234 and password == "admin":
        print("Login sucessfully")
        break 

    else:
        print("Re-enter the credentials")

else:
    print(" 3 attempts over")
    print("program is terminate")
