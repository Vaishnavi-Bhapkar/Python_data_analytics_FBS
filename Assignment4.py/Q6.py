## 6. WAP to check if a given number is prime number or not....

n = int(input("Enter number:"))
count = 0
for i in range (1, n+1):
    if n % 2== 0:
        count = count + 1
if count == 2:
    print("number is prime")
else:
     print("number is not prime")