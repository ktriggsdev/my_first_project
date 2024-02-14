bubblegum = 202
toffee = 118
ice_cream = 2250
milk_chocolate = 1680
doughnut = 1075
pancake = 80
total_income = bubblegum + toffee + ice_cream + milk_chocolate + doughnut + pancake



# Print the prices:
print("Earned amount:")
print("Bubblegum: ${}".format(bubblegum))
print("Toffee: ${}".format(toffee))
print("Ice cream: ${}".format(ice_cream))
print("Milk chocolate: ${}".format(milk_chocolate))
print("Doughnut: ${}".format(doughnut))
print("Pancake: ${}".format(pancake))
print()
print("\nIncome: ${:.2f}".format(total_income))
staff_expenses = input("Staff expenses:")
other_expenses = input("Other expenses:")
net_income = total_income - int(staff_expenses) - int(other_expenses)
print("\nNet income: ${:.2f}".format(net_income))