attendance = float(input("What is your attendance for this year? "))
exam = float(input("What was your exam percentage: "))
if (attendance > 90):
    if exam > 90:
        print ("Grade A")
    elif exam > 80 and exam <=90:
        print ("Grade B")
    elif exam > 70 and exam <= 80:
        print ("Grade C")
    elif exam <= 70:
        print ("Fail")
else:
    print ("Fail")