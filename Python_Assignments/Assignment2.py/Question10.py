    ## write a program to reverse three digit number...

num=int(input("enter three digit number:"))

a = num % 10
b = (num // 10) % 10
c= num // 100

reverse_number = a * 100 + b * 10 + c

print("reverse_number:",reverse_number)