import math
import datetime

def numInput(text):
    '''Attempt to convert user input to integer'''
    #Repeats until returns and breaks
    while True:
        user_input = str(input(text+": "))
        try:
            #Here attempt then return if no error
            int(user_input)
            return user_input
            break
        except:
            print ("Sorry, not a valid input.")

def inArray(item,array):
    '''Iterates through an array to check for an item'''
    for i in range (len(array)):
        if array[i] == item:
            return True
    return False

def checkDay(day,month,year):
    '''Returns True or False depending on a  valid day'''
    months31 = [1,3,5,7,8,10,12]
    months30 = [4,6,9,11]
    
    #Boundaries for months with 31 days, checking to see if month in that respective array
    if inArray(month, months31):
        if day < 1 or day > 31:
            return False
        else:
            return True
        
    #Boundaries for months with 30 days
    elif inArray(month, months30):
        if day < 1 or day > 30:
            return False
        else:
            return True
        
    #Boundaries for febuary, checking if leap year
    elif month == 2:
        if year % 4 == 0:
            if day < 1 or day > 29:
                return False
            else:
                return True
        else:
            if day < 1 or day >28:
                return False
            else:
                return True
        
def checkMonth(month):
    '''Returns True or False depending on a  valid month'''
    if int(month) > 13 or int(month) < 0:
        return False
    else:
        return True
    
def dayWord(day):
    if day == 0:
        print ("Monday")
    elif day == 1:
        print ("Tuesday")
    elif day == 2:
        print ("Wednesday")
    elif day == 3:
        print ("Thursday")
    elif day == 4:
        print ("Friday")
    elif day == 5:
        print ("Saturday")
    elif day == 6:
        print ("Sunday")
    else:
        print ("Something broke")
        
def daysSinceAD(year,month,day):
    difference = 0
    start = datetime.date(1,1,1)
    end = datetime.date(int(year),int(month),int(day))
    difference = end - start
    return (difference.days)

day = numInput("Enter a day in numbers")
month = numInput("Enter a month in numbers")
year = numInput("Enter a year in numbers")

#Checks the date, only if valid thecks month
valid = checkDay(day,month,year)
if valid == False:
    print ("Not a valid date")
else:
    valid = checkMonth(month)
    if valid == False:
        print ("Not a valid date")
    else:
        if int(year) > 0:
            print ("Valid date")
        else:
            print ("Sorry, years below 1AD are unsupported.")

day = daysSinceAD(year,month,day)
day = int(day) % 7
print (dayWord(day))

    
    
    
    
    