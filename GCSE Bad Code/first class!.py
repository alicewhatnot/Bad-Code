firstclass = str(input("is your letter first class: y/n"))
size = str(input("what is its size: (large letter/letter)"))
weight = int(input("what is the weight (gms): "))
cost = str(0)
if firstclass == "y":
    if size == "letter" and weight <= 100:
        (cost) = "1.65"
    if size == "large letter":
        if weight <= 100:
            (cost) = "1.95"
        elif weight <=250:
            (cost) = "2.37"
    else:
        (cost) = "2.81"
else:
    print ("needs to be first class")

print ("Your price is",(cost))
