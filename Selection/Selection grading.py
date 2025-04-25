#grading function
def grading(percentage):
    #grading 1-9
    if percentage < 9:
        print ("0")
    elif percentage < 20 and percentage > 9:
        print ("1")
    elif percentage < 30 and percentage > 19:
        print ("2")
    elif percentage < 40 and percentage > 29:
        print ("3")
    elif percentage < 50 and percentage > 39:
        print ("4")
    elif percentage < 60 and percentage > 49:
        print ("5")
    elif percentage < 70 and percentage > 59:
        print ("6")
    elif percentage < 80 and percentage > 69:
        print ("7")
    elif percentage < 90 and percentage > 79:
        print ("8")
    elif percentage > 89 and percentage < 101:
        print ("9")
    
#asking for the percentage
percentage = input("What percentage did you get in the exam?: ")

#verifying the percentage entered is between 0 and 100 and is digits
correctPercentageEntered = False
if percentage.isdigit():
    percentage = int(percentage)
    if percentage > 0 and percentage < 100:
        correctPercentageEntered = True
        
#once found to be incorrect, the user is asked again for the percentage
while correctPercentageEntered == False:
    print ("Invalid input, percentage entered must be an integer")
    percentage = input("What percentage did you get in the exam?: ")
    if percentage.isdigit():
        percentage = int(percentage)
        if percentage > 0 and percentage < 100:
            correctPercentageEntered = True

#calling the function
grading(percentage)