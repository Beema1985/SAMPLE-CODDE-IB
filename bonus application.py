sales = 0
count = int(input("Enter number of sales: "))
for i in range(count):
    print(" Sale", i + 1,)
    name = input("Enter worker's name: ")
    product = input("Enter product name: ")
    price = float(input("Enter sale price: "))

    
    if price > 500000:
        bonus = price * 0.20
    elif price > 100000:
        bonus = price * 0.15
    elif price > 75000:
        bonus = price * 0.10
    elif price > 50000:
        bonus = price * 0.05
    else:
        bonus = 0

    sales = sales + price

    print("Worker:", name)
    print("Product:", product)
    print("Sale:", price)
    print("Bonus:",round(bonus,3))


average = sales / count
print("Total Sales Amount:", sales)
print("Average Sale Amount:", round(average, 2))
