## Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount....

amount = int(input("Enter amount: "))

n = amount // 500
amount %= 500

n += amount // 200
amount %= 200

n += amount // 100
amount %= 100

n += amount // 50
amount %= 50

n += amount // 20
amount %= 20

n += amount // 10
amount %= 10

n += amount // 5
amount %= 5

n += amount // 2
amount %= 2

n += amount

print("Minimum number of notes:", n)