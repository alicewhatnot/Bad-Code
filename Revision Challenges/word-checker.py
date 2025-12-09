#Time Taken: 4:45
#Marks Worth: 12

valid = True
firstWord = str(input("Enter the first word: "))
secondWord = str(input("Enter the second word: "))
secondArray = []

for char in secondWord:
    secondArray.append(char)

for char in firstWord:
    if char in secondArray:
        secondArray.remove(char)
    else:
        valid = False
 
if not valid:
    print ("The second word cannot be created using the first.")
else:
    print ("The second word can be created with the first")