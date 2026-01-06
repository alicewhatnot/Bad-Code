    
def harshard(n): 
    harshardTotal = 0
    number = 1    

    while harshardTotal != n:
        digitsum = 0
        strNum = str(number)

        for i in range (len(strNum)):
            digitsum += int(strNum[i])

        if number % digitsum == 0:
            harshardTotal += 1
            harshardNum = number
            number += 1
        else:
            number += 1
    
    return harshardNum

harshardn = int(input("Which harshard to return: "))
print (harshard(harshardn))