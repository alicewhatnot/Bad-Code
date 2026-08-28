#65 - 90 FOR CAPITALS
#97 - 122 FOR LOWERCASE

def checkSpecialCharacters(string):
    for i in range (len(string)-1):
        if ord(string[i]) < 65 or ord(string[i]) > 90:
            if ord(string[i]) < 97 or ord(string[i]) > 122:
                string = string[:i] + string[(i+1):]
                i = i - 1
                
    print (string)
    return string

def cipherString(string,rows):
    cipher_string = []

    for row in range (0,rows):
        for i in range (0,len(string)-1,rows):
            cipher_string.append(string[i+row])
    return cipher_string

def printArray(array):
    for i in range (len(array)):
        print (array[i], end="")
        
string = str(input("Enter the string to be encoded: "))
try:
    rows = int(input("Enter the number of rows for encoding: "))
except:
    print("Not an integer amount")

string = checkSpecialCharacters(string)

while (len(string) % rows != 0):
    string = string + " "
    
cipher_string = cipherString(string,rows)

printArray(cipher_string)


