d = {}
total_bonus = 0
n = int(input("Enter number of employees: "))

for i in range(n):
    sales = int(input(f"\nEnter sales for employee {i+1}: "))

    if sales >= 500000:
        print("bonus is 20000 that will be incremented in your salary")
    elif 100000 < sales < 500000:
        print("bonus is 15000 that will be incremented in your salary")
    elif 75000 < sales <= 100000:
        print("bonus is 10000 that will be incremented in your salary")
    elif 50000 < sales <= 75000:
        print("bonus is 5000 that will be incremented in your salary")
    else:
        print("you can't get any bonus because your sales is less than or equal to 50000")

    
    if sales >= 500000:
        bonus = 20000
    elif 100000 < sales < 500000:
        bonus = 15000
    elif 75000 < sales <= 100000:
        bonus = 10000
    elif 50000 < sales <= 75000:
        bonus = 5000
    else:
        bonus = 0

    d[f"Employee_{i+1}"] = bonus
    total_bonus += bonus

print("\nBonus Summary:")
for employee, bonus in d.items():
    print(f"{employee}: ₹{bonus}")
    
average_bonus = total_bonus / n
print(f"\nAverage Bonus Given: ₹{average_bonus:.2f}")
