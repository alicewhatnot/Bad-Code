passwordCorrect = False
password = str(input("Enter the password: "))
if password == "Tues1212":
    passwordCorrect = True
    print ("Password accepted.")
count = 0
while passwordCorrect == False and count < 2:
    count = count + 1
    password = str(input("That was incorrect, enter the password again: "))
    if password == "Tues1212":
        passwordCorrect = True
        print ("Password accepted.")
if count == 2:
    print ("No more password guesses remaining.")