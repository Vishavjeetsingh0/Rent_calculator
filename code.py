rent=int(input("Total rent"))
electricity_units=int(input("Total electricity units spend"))
charge_per_unit=int(input("Electricity charge per unit"))
persons=int(input("No of persons  to divide the amount"))

total_bill= electricity_units * charge_per_unit

output=(rent + total_bill)//persons

print(output)