## Find Component Interest 

P = int(input('Enter a Principal:'))
R = int(input('Enter a Rate:'))
T = int(input('enter a Time:'))

amount = P * (1 + R / 100 ) ** T 
compound_intrest = amount - P


print('compound intrest:',compound_intrest)

 