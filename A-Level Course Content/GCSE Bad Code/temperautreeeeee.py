Month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
temperature = 0
temperatureArray = ["","","","","","","","","","","",""]

for i in range (0,12):
    print ("Enter a temperature for", Month[i])
    temperature = float(input())
    temperatureArray[i] = temperature

for i in range (0,len(Month)):
    print ("In", Month[i], "the temperature was", temperatureArray[i])