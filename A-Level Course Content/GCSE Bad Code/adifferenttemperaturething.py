month = ["January","Febuary","March","April","May","June","July","august ","September","October","November","December"]

RainfallValues=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
TotalRainfall = 0
AverageRainfallMonth = 0
MonthAboveAverage = 0
for i in range(len(month)):
   print( "Enter the rainfall for" ,month[i])
   x = float(input())
   RainfallValues[i] = x

for i in range(len(month)):
   TotalRainfall = TotalRainfall + RainfallValues[i]

AverageRainfallMonth = TotalRainfall /  len(month)
print( "the monthly average over a year is", AverageRainfallMonth)

for i in range(len(month)):
   if RainfallValues[i] > AverageRainfallMonth :
      MonthAboveAverage = MonthAboveAverage + 1


print("There is", MonthAboveAverage,"months above average value")