def createList(n):
    listShop = []
    while True:
        item = str(input(f"Enter something to add to shopping list {n} or x to stop: "))
        if item == "x":
            break
        else:
            listShop.append(item)
    return listShop

def createUniqueList(list1,list2):
    temp1 = list1[:]
    temp2 = list2[:]
    
    if len(temp1) >= len(temp2):
        shortList = temp2
        longList = temp1
    else:
        shortList = temp1
        longList = temp2
        
    for i in range(len(shortList) - 1, -1, -1):
        for j in range(len(longList) - 1, -1, -1):  
            if shortList[i] == longList[j]:
                longList.pop(j)  
                shortList.pop(i)  
                break
            
    uniqueList = temp1 + temp2
    return uniqueList
            
def combineLists(list1,list2):
    temp1 = list1[:]
    temp2 = list2[:]
    
    if len(temp1) >= len(temp2):
        shortList = temp2
        longList = temp1
    else:
        shortList = temp1
        longList = temp2
        
    for i in range(len(shortList) - 1, -1, -1):
        for j in range(len(longList) - 1, -1, -1):  
            if shortList[i] == longList[j]:
                longList.pop(j)    
                break
    
    combinedList = temp1 + temp2
    return combinedList

def printList(listt):
    for i in range (len(listt)-1):
        print (listt[i],end=", ")
    print (listt[len(listt)-1])
    
list1 = createList(1)
list2 = createList(2)
uniqueList = createUniqueList(list1,list2)
combinedList = combineLists(list1,list2)
if len(uniqueList) == 0:
    print("There are no unique items.")
else:
    print ("The unique items are: ",end = "")
    printList(uniqueList)
    print ("")
print ("The combined list is: ",end = "")
printList(combinedList)