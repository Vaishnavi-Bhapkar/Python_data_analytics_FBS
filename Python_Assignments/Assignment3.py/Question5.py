     ## check whether is given triangle is equilateral , scalene and isosceles....

a = float(input("Enter angle:"))
b = float(input("Enter angle:"))
c = float(input("Enter angle:"))

if a == b == c:
    print("triangle is equilateral")
elif a == b or b == c or a == c :
    print("triangle is isosceles")
else:
    print("triangle is scalene")