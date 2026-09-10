num = int(input("enter three digit number: "))

first = num // 100
second = (num // 10) % 10
third = num % 10

if (first == 2 * second and first == third / 2):
    print("yes")
else:
    print("try next time")
