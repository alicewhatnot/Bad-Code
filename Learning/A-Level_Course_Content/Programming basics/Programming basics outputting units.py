number = int(input("Enter a three digit number: "))
hundreds = number // 100
remainder = number % (hundreds*100)
tens = remainder // 10
remainder = remainder % (tens*10)
units = remainder
print (hundreds,tens,units)