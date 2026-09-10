# Enter 5 sub marks and display grade...

S1 = int(input("enter subject1 marks:"))
S2 = int(input("enter subject2 marks:"))
S3 = int(input("enter subject3 marks:"))
S4 = int(input("enter subject4 marks:"))
S5 = int(input("enter subject5 marks:"))

Total = 150
marks = S1 + S2 + S3 + S4 + S5
percentage = (marks / 150) * 100

print("Percentage:",percentage)

if (percentage >= 90):
    print("First class")

elif (percentage >=75):
    print("Second class")

elif (percentage >= 60):
    print("Third class")

else:
    (percentage <= 59)
    print("Failed")