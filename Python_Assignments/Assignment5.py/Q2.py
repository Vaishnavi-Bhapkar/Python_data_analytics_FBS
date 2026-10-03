 ## Enter number of students from user For those many students accept marks of 5 subject marks from user and calculate percentage. Display all percentage and
 ## average percentage of students.....

n = int(input("Enter no.of user:"))
total_marks = 150
total_percentage = 0

for i in range (n):
    print("enter students marks", i + 1)

    m1=int(input(" subject 1 :"))
    m2=int(input(" subject 2 :"))
    m3=int(input(" subject 3 :"))
    m4=int(input(" subject 4 :"))
    m5=int(input(" subject 5 :"))

    sum = m1 + m2 + m3 + m4 + m5
    percentage = sum / total_marks * 100

print("percentage:",percentage)
total_percentage = total_percentage + percentage

average = total_percentage / n

print("Average percentage =", average)



        
    

