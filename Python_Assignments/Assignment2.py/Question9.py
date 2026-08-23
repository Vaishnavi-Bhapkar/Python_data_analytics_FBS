## Swap numbers without using third number....

a = int(input("Enter a:"))
b = int(input("Enter b:"))

print(f"before swapping:a ={a},  b={b}")

a = a + b
b= a - b
a= a-b

print(f"after swapping: a={a}")
print(f"after swapping: b={b}")