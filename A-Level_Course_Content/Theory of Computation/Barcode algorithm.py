barcode = 0
digits = [0,0,0,0,0,0]
totalCorrect = 0
for i in range (1):
    barcode = str(input("Enter a barcode: "))
    for i in range (6):
        digits[i] = int(barcode[i])
    weightTotal = int(digits[0]+digits[1]*3+digits[2]+digits[3]*3+digits[4])
    if weightTotal % 10 == digits[5]:
        totalCorrect = totalCorrect + 1
print (f"There were {totalCorrect} total correct barcodes.")
        
    