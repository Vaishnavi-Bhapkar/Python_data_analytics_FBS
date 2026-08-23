    ##  calculate selling price of book based on cost price and discount..

cost_price = int(input("enter cost price:"))
discount = int(input("enter discount:"))

selling_price = cost_price - (cost_price * discount / 100 )


print("selling_price:",selling_price)

