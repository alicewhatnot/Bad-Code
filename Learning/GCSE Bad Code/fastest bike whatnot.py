fastest = float("inf")
time = float(input("Enter a time or -1 to finish "))
while time != -1:
    if fastest > time:
        fastest = time
    time = float(input("Enter a time or -1 to finish "))
        
print ("the fastest was",fastest)
        
