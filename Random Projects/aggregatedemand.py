# AD = C + I + G + X - M

# Consumption
# Investment
# Government Spending
# Net Exports

consumption = int(input("Enter the consumption: "))
investment = int(input("Enter the investment: "))
govspending = int(input("Enter the government spending: "))
netexports = int(input("Enter the net exports: "))

aggregatedemand = consumption + investment + govspending - netexports

print(f"The aggregate demand is {aggregatedemand}")