name = ["Alice","Ellie","Rosie"]
found = False
nameSearch = input("Enter a name to search for: ")
for i in range (len(name)):
    if nameSearch == name[i]:
        print ("The students record number is:",i+1)
        found = True
if found == False:
    print ("Name was not found.")

