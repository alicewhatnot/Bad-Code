daytime = []
nighttime = []

for month in range (0,30):
    # this validates the input of midday and stores it in the array daytime[]
    dayTempInput = "false"
    while dayTempInput == "false":
        dayTemp = float(input("Enter the temperature from midday: "))
        if (-50 < dayTemp < 60) and (dayTemp != ""):
            dayTempInput = "true"
        else:
            print ("Sorry, your entry was not valid.")
    daytime.append(dayTemp)

    # this validates the input of midnight and stores it in the array midnight[]
    nightTempInput = "false"
    while nightTempInput == "false":
        nightTemp = float(input("Enter the temperature from midnight: "))
        if (-50 < nightTemp < 60) and (nightTemp != ""):
            nightTempInput = "true"
        else:
            print ("Sorry, your entry was not valid.")
    nighttime.append(nightTemp)

# this calculates the average temperature for midday and midnight and then outputs it
daytimeTotal = 0
daytimeAverage = 0
for i in range (0,len(daytime)):
    daytimeTotal = daytimeTotal + daytime[i]
daytimeAverage = daytimeTotal/len(daytime)
print ("")
print ("The average temperature during the day was",daytimeAverage)

nighttimeTotal = 0
nighttimeAverage = 0
for i in range (0,len(nighttime)):
    nighttimeTotal = nighttimeTotal + nighttime[i]
nighttimeAverage = nighttimeTotal/len(nighttime)
print ("The average temperature during the night was",nighttimeAverage)

# calculating the maximum day and minimum night temperatures
daytimeMax = 0
maxDay = 0
for i in range (0,len(daytime)):
    if daytime[i] > daytimeMax:
        daytimeMax = daytime[i]
        maxMonth = (i)
        
nighttimeMin = float('inf')
minNight = 0
for i in range (0,len(nighttime)):
    if nighttimeMin > nighttime[i]:
        nighttimeMin = nighttime[i]
        minNight = (i)
        
match maxDay:
    case 0:
        formatDay = "st"
    case 1:
        formatDay = "nd"
    case 2:
        formatDay = "rd"
    case _:
        formatDay = "th"
match minNight:
    case 0:
        formatNight = "st"
    case 1:
        formatNight = "nd"
    case 2:
        formatNight = "rd"
    case _:
        formatNight = "th"
        
# outputting the maximum day and minimum night temperatures
print ("")
print ("The maximum midday temperature was",daytimeMax,"on the",maxDay+1,formatDay)
print ("The minimum midnight temperature was",nighttimeMin,"on the",minNight+1,formatNight)