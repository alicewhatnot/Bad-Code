def menu():
    choiceEntered = False
    while choiceEntered == False:
        print ("Enter 1 to input names\n"
               "Enter 2 to output all names\n"
               "Enter 3 to quit")
        choice = str(input())
        if choice == "1":
            return choice
            choiceEntered = True
        elif choice == "2":
            return choice
            choiceEntered = True
        elif choice == "3":
            return choice
            choiceEntered = True
        else:
            print("Sorry, Invalid input")
        
def inputNames():
    finished = "n"
    while finished != "y":
        name = str(input("Enter a name:"))
        text_file = open("names.txt","a")
        text_file.write(name)
        text_file.write("\n")
        text_file.close()
        finished = str(input("Finished entering names? (y/n)"))
        
def readNames():
    try: text_file = open("names.txt","r")
    except:
        print ("Sorry, there are no names in the file")
        return
    lines = text_file.readlines()
    for line in lines:
        print(line)

def exit():
    exiting = str(input("Do you wish to exit? (y/n)"))
    if exiting == "y":
        return True
    
# MAIN CODE

exiting = False
while True:
    choice = menu()
    if choice == "1":
        inputNames()
    if choice == "2":
        readNames()
    if choice == "3":
        exiting = exit()
    if exiting == True:
        break
    
    
