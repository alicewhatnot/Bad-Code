import datetime
import random

while True:
    def bubbleSort(array):
        swapMade = True
        while swapMade == True:
            swapMade = False
            for position in range (0,len(array)-1):
                if array[position] > array[position+1]:
                    temp = array[position]
                    array[position] = array[position+1]
                    array[position+1] = temp
                    swapMade = True
                    
    def insertionSort(array):
        for position in range (1,len(array)):
            nextPos = array[position]
            i = position - 1
            while i >= 0 and array[i] > nextPos:
                array[i+1] = array[i]
                i = i-1
            array[i+1] = nextPos

    def mergeSort(array):
    #    print("Splitting ",alist)
        if len(array)>1:
            mid = len(array)//2
            lefthalf = array[:mid]
            righthalf = array[mid:]

            mergeSort(lefthalf)
            mergeSort(righthalf)

            i=0
            j=0
            k=0
            while i<len(lefthalf) and j<len(righthalf):
                if lefthalf[i]<righthalf[j]:
                    array[k]=lefthalf[i]
                    i=i+1
                else:
                    array[k]=righthalf[j]
                    j=j+1
                k=k+1

            while i<len(lefthalf):
                array[k]=lefthalf[i]
                i=i+1
                k=k+1

            while j<len(righthalf):
                array[k]=righthalf[j]
                j=j+1
                k=k+1

    def bogoSort(array):
        alrSorted = False
        while alrSorted == False:
            alrSorted = True
            for position in range (len(array)-1):
                if array[position] > array[position+1]:
                    alrSorted = False
            if alrSorted == False:
                random.shuffle(array)
            
    def defineArray():
        arrayLength = int(input("Enter how long you want the array to be: "))
        array = [(random.randint(1,10000)) for k in range (arrayLength)]
        sortType = input("Enter:\n"
                         "b for bubble\n"
                         "bo for bogo\n"
                         "m for merge\n"
                         "i for insertion\n")
        return array,sortType


    array,sort = defineArray()
    t0 = datetime.datetime.now()
    if sort == "b":
        bubbleSort(array)
    elif sort == "bo":
        bogoSort(array)
    elif sort == "m":
        mergeSort(array)
    elif sort == "i":
        insertionSort(array)
        
    t1 = datetime.datetime.now()
    print (f"Program executed with a run time of {t1-t0}.")
    print (array)

