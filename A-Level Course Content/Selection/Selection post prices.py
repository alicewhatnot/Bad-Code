code1 = float(5)
code2 = float(3.5)
orderValue = float(input("Enter the value of your order: "))
if orderValue >= 15:
    postalCharge = float(0)
else:
    postalCharge = code2
paidDelivery = str(input("Pay for guaranteed next day delivery? (y/n)"))
if paidDelivery == "y":
    postalCharge = code1
print ("The overall charge will be £",(postalCharge + orderValue))
