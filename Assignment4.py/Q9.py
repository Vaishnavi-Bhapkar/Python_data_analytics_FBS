 ##  WAP to print all numbers in a range divisible by a given number....

start = int(input("Enter start range:"))
end = int(input("Enter end range:"))

for i in range (start , end + 1):
    if i % 5 == 0:
        print(i)
