# Write a program to prompt user to enter userid and password. After verifyinguserid and password display a 4 digit random number and
#  ask user to enter the same. If user enters the same number then show him success message otherwise failed. (Something like captcha).....

import random

userid = int(input("Enter userid:"))
password =int(input("Enter password:"))

if userid == 1234  and password == 1234 :
 num=random.randint(1000,9999)
 print("Verification Number:", num)
    
entered_num = int(input("Enter the same number:"))

if (entered_num == num):
    print("sucesssfully log in")
else:
    print("failed to log in ")