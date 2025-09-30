file = open("membershipDetails.txt", "w")
file.write ("Memberships:")
file.write ('\n')
file.close()

moreMembers = True
while moreMembers == True:
    print ("Enter the following membership details for the Rock Climbing Club.")
    name = str(input("Name: "))
    age = str(input("Age: "))
    gender = str(input("Gender: "))
    phoneNumber = str(input("Phone Number: "))
    email = str(input("Email: "))
    savingDetails = False
    print ("These are the details you entered:")
    print ("Name: ",name)
    print ("Age: ",age)
    print ("Gender: ",gender)
    print ("Phone number:",phoneNumber)
    print ("Email: ",email)
    customerSavingDetails = str(input("Submit details to the system? (y/n)"))
    if customerSavingDetails == "y":
        file = open('membershipDetails.txt','a')
        file.write("Name:"+name)
        file.write(" Age:"+age)
        file.write(" Gender:"+gender)
        file.write(" Phone number:"+phoneNumber)
        file.write(" Email:"+email)
        file.write('\n')
        
    continuing = str(input("Enter another membership? (y/n) or s to search members"))
    if continuing == "n":
        moreMembers = False
    elif continuing == "s":
        name = str(input("Enter the name you wish to find: "))
        try:
            with open('membershipDetails.txt') as file:
                for line in file:
                    if name in line:
                        print(line.strip())
        except FileNotFoundError:
            print("Sorry, no memberships under that name.")
        except Exception as e:
            print("Whoops! something went wrong.")
                    
                

    

    