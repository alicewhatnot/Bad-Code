import random

def search(array,value):
    low = 0
    high = len(array)
    found = False
    while found == False:
        middle = int((low + high)/2)
        if middle == 1:
            print ("The data has NOT been found in the array.")
            return
        try:
            if array[middle] == value:
                found = True
                print ("The data has been found in the array.")
                return
            else:
                if array[middle] > value:
                    high = middle - 1
                else:
                    low = middle + 1
        except:
            print ("The data has NOT been found in the array.")
            return

array = ["1","2","3","4","5","6","7","8","9"]
value = str(input("Enter the data you want to check if is present in the array: "))
search(array,value)
        