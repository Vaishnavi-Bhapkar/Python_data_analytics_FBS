          ## Calculate percentage of students  

sub1=int (input('Enter marks of subjects1:' ))
sub2=int (input('Enter marks of subjects2:' ))
sub3=int (input('Enter marks of subjects3:' ))
sub4=int (input('Enter marks of subjects4:' ))
sub5=int (input('Enter marks of subjects5:' ))

##  percentage = obtainedmarks /  totalmarks  * 100 


total_marks = 150
obtained_marks = sub1 + sub2 + sub3 + sub4 + sub5 
percentage = (obtained_marks) / total_marks * 100

print('percentage of students:',percentage)