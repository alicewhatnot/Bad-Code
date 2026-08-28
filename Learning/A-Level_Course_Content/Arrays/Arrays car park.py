# clears the parking grid by iteration over the whole 2D array
def clearParking (gridParking):
    ''' clears the parking grid '''
    for row in range(10):
        for column in range(6):
            gridParking[row][column] = "empty"
    return gridParking

# asks user to enter a registration into the array with validation
def registrationAndParking ():
    '''Collect registration and parking details '''
    # assumes the data entered is wrong
    verified = False
    emptyReference = False
    registration = input("Enter the registration: ")
    row = int(input("Enter the row parked in: "))
    column = int(input("Enter the column parked in: "))
    # checks to see if data entered is right
    if row >= 1 and row <= 10 and column >= 1 and column <= 6:
        verified = True
    # repeats asking the user to enter the data when it is not right, does this several times with the different data types
    while verified == False:
        print ("Sorry, that was not a valid input.")
        registration = input("Enter the registration: ")
        row = int(input("Enter the row parked in: "))
        column = int(input("Enter the column parked in: "))
        if row >= 1 and row <= 10 and column >= 1 and column <= 6:
            verified = True
            return verified
    if gridParking[row-1][column-1] == "empty":
        emptyReference = True
    while emptyReference == False:
        print ("Sorry, that space is taken.")
        registration = input("Enter the registration: ")
        row = int(input("Enter the row parked in: "))
        column = int(input("Enter the column parked in: "))
        if gridParking[row-1][column-1] == "empty":
            emptyReference = True
            return emptyReference
    gridParking[column-1][row-1] = registration

#iterates through the array, printing it as it goes
def showParking ():
    ''' shows the array parking grid '''
    for i in range (10):
        print (gridParking[i])

#removing a car
def removeCar ():
    car = str(input("Enter the registration of your car: "))
    found = False
    for row in range(10):
        for column in range(6):
            if gridParking[row][column] == car:
                gridParking[row][column] = "empty"
                print ("Car removed.")
                found = True
    if found == False:
        print ("Car not found.")
    
#main code
gridParking = [["empty" for _ in range(6)] for _ in range(10)]
while True:
    print ('''
1 To clear parking
2 To enter a car into the car park
3 To show the car park
4 To remove a car ''')
    choice = str(input("Enter choice here: "))
    if choice == "1":
        clearParking(gridParking)
    if choice == "2":
        registrationAndParking()
    if choice == "3":
        showParking()
    if choice == "4":
        removeCar()
    
