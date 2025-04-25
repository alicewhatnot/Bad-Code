temperature = str(input("Do you have a temperature? (y/n)"))
if temperature == "y":
    throat = str(input("Is your throat sore? (y/n)"))
    if throat == "y":
        print ("You may have a throat incetion")
    else:
        cough = str(input("Do you have a cough? (y/n)"))
        if cough == "y":
            print ("You have a chest infection")
        else:
            print ("Just get some rest then")
else:
    print ("Well why are you even here then.")
            