           ## Find the sum of three digits..

number = int(input("Enter a three digit number:"))

ones = number % 10
tense = (number // 10) % 10 
hundred = number // 100

digit_sum =  hundred + tense + ones  


print("digit_sum:",digit_sum)