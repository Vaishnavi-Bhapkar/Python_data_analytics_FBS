 ## Convert Time into Hour , min , sec 

Time= int(input("Enter Time:"))

Hour= Time // 60 
sec = (Time % 60)%60 

print("Hour:",Hour)
print("sec:",sec)