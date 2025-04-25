import math

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
        if int(year) > 1750:
            print ("Valid date")
        else:
            print ("Sorry, years below 1750 are unsupported.")

def yearCode(year):
    '''Convert year to yearcode for calc'''
    #Adds a quarter of the last 2 digits of the year to 1/4 of itself
    last2 = year[-2:]
    quarter = int(last2) / 4
    quarter = math.trunc(quarter)
    yearCode = (int(last2) + int(quarter)) % 7
    return yearCode

def monthCode(month):
    '''convert month to monthcode for calc'''
    #Codes found from reddit x
    if 2 < int(month) < 4:
        monthCode = 33
    elif 3 < int(month) < 7:
        monthCode = 614
    elif 7 < int(month) < 10:
        monthCode = 625
    else:
        monthCode = 35
    return monthCode

def centuryCode(year):
    '''convert year to centurycode for calc'''
    first2 = year[:2]
    calc = (int(first2) - 17) % 4
    if calc == 0:
        centuryCode = 4
    elif calc == 1:
        centuryCode = 2
    elif calc == 2:
        centuryCode = 0
    elif calc == 3:
        centuryCode = 6
    return centuryCode

def leapModifier(year,day):
    '''removing days if the year is a leapyear'''
    dateCode = day
    year = int(year)
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        dateCode = int(dateCode) - 1
    return dateCode

yearCode = yearCode(year)
monthCode = monthCode(month)
centuryCode = centuryCode(year)
dateCode = leapModifier(year,day)
namedDay = (int(yearCode) + int(monthCode) + int(centuryCode) + int(dateCode)) % 7
dayWord(namedDay)


    
    
    
    
    
    