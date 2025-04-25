maximum = []
minimum = []
tempMax = 0
day = 0
while tempMax != 999:
    day = day + 1
    tempMax = int(input(f"Enter the maximum temperature for day {day}: "))
    if tempMax != 999:
        maximum.append(tempMax)
        tempMin = int(input(f"Enter the minimum temperature for day {day}: "))
        minimum.append(tempMin)

noDays = 0
total = 0
average = 0
for day in range (0,len(maximum)):
    average = ((maximum[day] + minimum[day])/2)
    total = total + average
    noDays = noDays + 1

average = total/noDays
print (f"The average temperature was {average}.")
daysAboveAv = 0
daysNegative = 0
for day in range (0,len(maximum)):
    if ((maximum[day]+minimum[day])/2) > average:
        daysAboveAv = daysAboveAv + 1
    if maximum[day] < 0 or minimum[day] < 0:
        daysNegative = daysNegative + 1

print (f"There were {daysAboveAv} days above the average temperature.")
print (f"There were {daysNegative} days with a negative temperature.")

    
    