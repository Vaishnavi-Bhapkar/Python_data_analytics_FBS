  #  WAP to print Armstrong number within a given range...

start = int(input("Enter start range:"))
end = int(input("Enter end range:"))

for n in range (start,end +1):
    a = n
    sum = 0

    
    while a > 0:
        r = a % 10
        sum = sum + r ** 3
        a = a // 10

    if sum == n:
        print(n)



