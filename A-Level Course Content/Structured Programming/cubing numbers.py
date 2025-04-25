for number in range (100,100000000):
    firstDigit = number//100
    remainder = number%100
    secondDigit = remainder//10
    thirdDigit = number%10
    total = firstDigit*firstDigit*firstDigit
    total = secondDigit*secondDigit*secondDigit + total
    total = thirdDigit*thirdDigit*thirdDigit + total
    if total == number:
        print (total)
print ("done")
