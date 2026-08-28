#Time Taken: 5.44
#Marks Worth: 12

def harshard(number: int):
    strNum = str(number)
    total = 0
    for i in range (len(strNum)):
        total += int(strNum[i])

    return number % total == 0

nth = int(input("Which harshard number should be returned: ")) 
harshardTotal = 0
number = 0

while harshardTotal < nth:
    number += 1
    if harshard(number):
        harshardTotal += 1

print (f"{number} is harshard {nth}.")