school = ["AAAA","BBBB","CCCC","DDDD"]
medal = [4,7,1,3]

# while loop to keep entering medals until -1 is entered
while True:
    # asking for and verifying the school number
    verified = False
    while verified == False:
        print ("Enter school number: ")
        schNum = int(input())
        if schNum == 1 or schNum == 2 or schNum == 3 or schNum == 4:
            verified = True
        # breaking out of verification loop and printing results if -1 entered
        elif schNum == -1:
            
            for i in range (4):
                print (f"School Number: {i+1} School Name: {school[i]} Number of medals: {medal[i]}")
                
            break
        else:
            print ("The entry wasn't quite right - try again")
    
    # breaking out of while loop also if enters -1
    if schNum == -1:
        break
    
    # asking for and verifying number of medals to be added
    verified = False
    while verified == False:
        print (f"Enter the number of medals to add to school {schNum}:")
        numMedals = int(input())
        print (f"Did you mean to enter {numMedals} medals? (y/n):")
        reEnter = input()
        if reEnter == "y":
            verified = True
            
        # performing the medal total updates
        medal[schNum-1] = medal[schNum-1] + numMedals
        