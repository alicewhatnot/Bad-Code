outletSales = [[10,12,15,10],[5,8,3,6],[10,12,15,10]]
total = [0,0,0,0]
for quarter in range (0,4):
    for outlet in range (0,3):
        total[quarter] = total[quarter] + outletSales[outlet][quarter]
    print (f"Total for quarter {quarter+1} is: {total[quarter]}")