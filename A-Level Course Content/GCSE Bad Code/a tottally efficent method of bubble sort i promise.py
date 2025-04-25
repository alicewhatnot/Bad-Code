names = ["Toby","Abdul","Gale","Ruby","Amy","Boris"]
numItems = 0
flag = "false"
numItems = len(names) -1
while numItems > 1:
    for item in range (0,numItems):
        if names[item] > names[item+1]:
            temp = names[item]
            names[item] = names[item+1]
            names[item+1] = temp
#       elif names[item] < names[item+1]:
#           flag = "true"
#   if flag == "true":
#       break
    numItems = numItems - 1
numItems = len(names)
for i in range(0,numItems):
    print (names[i])