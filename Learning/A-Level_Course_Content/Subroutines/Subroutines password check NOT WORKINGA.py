def getPsword(attempt):
    lenCheck = False
    while lenCheck == False:
        if attempt == 1:
            print ("Enter password:")
        else:
            print ("enter password again:")
        pswd = input
        if pswd.len < 6 or pswd.len > 8:
            print ("Error. Password must be 6 to 8 characters long")\
            pswd = input
        else:
            lenCheck = True
            return pswd

# MAIN CODE #
count = 0
pswd1 = a
pswd2 = b
while pswd2 != pswd1:
    if count > 0:
        print ("Error - passwords do not match")
    count = count + 1
    attempt = 1
    pswd1 = getPsword(attempt)
    attempt = 2
    pswd2 = getPsword(attempt)
print ("Password change successful")