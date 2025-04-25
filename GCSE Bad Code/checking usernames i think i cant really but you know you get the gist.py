username = input("Enter your username: ")
def usernamechecks(username)
    usernameEntered = "false"
    while usernameEntered == "false":
        username = input("Enter your username: ")
        if username != "":
            if len(username) < 8:
                usernameEntered = "false"
            else:
                usernameEntered = "true"
            return usernameEntered
                
usernamechecks

print ("Your username is:",username)


        
