def calculate_bonus(sales):
    if sales > 500000:
        return sales * 0.20
    elif sales > 100000:
        return sales * 0.15
    elif sales > 50000:
        return sales * 0.10
    else:
        return 0

n = int(input("How many employees? "))
total_sales = 0
bonuses = []

for i in range(n):
    sales = float(input(f"Sales for employee {i+1}: ₹"))
    bonus = calculate_bonus(sales)
    bonuses.append((sales, bonus))
    total_sales += sales

print("--- Bonus Report ---")
for i, (sales, bonus) in enumerate(bonuses, 1):
    print(f"Employee {i}: Sales = ₹{sales:.2f}, Bonus = ₹{bonus:.2f}")

average = total_sales / n
print(f"Average Sales = ₹{average:.2f}")
