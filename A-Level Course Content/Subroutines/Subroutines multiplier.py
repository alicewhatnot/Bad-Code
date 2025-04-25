def multiples(table,startNum,endNum,pupilName):
    print ("These are the times tables you requested",pupilName,":")
    for multiples in range (startNum,endNum+1): 
        print (f"{table}x{multiples} = {table*multiples}")

print ("Enter your name: ")
pupilName = input()
print ("Enter the times table, start number and end number: ")
table = int(input())
startNum = int(input())
endNum = int(input())
multiples(table,startNum,endNum,pupilName)