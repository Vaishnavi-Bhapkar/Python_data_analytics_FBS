            ## check triangle is valid or not using sides...


a = int(input("Enter side:"))
b = int(input("Enter side:"))
c = int(input("Enter side:"))

if a > 0 and b > 0 and c > 0 and a + b > c and b +c >a and c + a > b :
    print("triangle is valid")
else:
    print("triangle is invalid")