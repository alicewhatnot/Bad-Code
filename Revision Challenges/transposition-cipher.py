plainText = str(input("Enter the text to be encrypted: "))

divisor = 0
while not (0 < divisor and divisor < 100):
    divisor = str(input("Enter the number of columns: "))
    try:
        divisor = int(divisor)
    except:
        divisor = 0

    if divisor == 0:
        print ("Columns out of range")

cipherText = ""

if divisor > len(plainText):
    cipherText = plainText

for i in range (divisor):
    for j in range (len(plainText)//divisor):
        try:
            cipherText += plainText[j*(divisor)+i]
        except:
            break

print (cipherText)