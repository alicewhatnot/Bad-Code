import random

userChoice = int(input("Enter the size of the list: "))
list = []
removeList = []
for i in range (userChoice):
    list.append(random.randint(1, 100))

count = 0

for i in range (len(list)):
    try:
        if 80 <= list[i] <= 100:
            count = count + 1
            list.pop(i)
    except:
        break
    
print (f"The numbers 80-100 were found {count} times.")
