numbers = [0,0,0,0,0,0]
total = 0
for i in range (6):
    numbers[i] = int(input("Enter a number: "))
    total = total + numbers[i]
for i in range (5,-1,-1):
    print (numbers[i])
print (total)
print (total/6)