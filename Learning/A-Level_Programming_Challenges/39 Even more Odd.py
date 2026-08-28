def bubbleSort(array):
    for i in range (len(array)-1):
        for j in range (len(array)-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array
    
array = [11,5,8,4,6,9,4,3,8,1]
array_even = []
array_odd = []

print ("Initial array is: ")
for index in range (len(array)):
    if array[index] % 2 == 0:
        array_even.append(array[index])
    else:
        array_odd.append(array[index])
    print (str(array[index]) + ", ", end = "")

print ("")
array_even = bubbleSort(array_even)
array_odd = bubbleSort(array_odd)
final_array = []

for index in range (len(array_odd)):
    final_array.append(array_odd[index])
    
for index in range (len(array_even)):
    final_array.append(array_even[index])
    
print ("Output array is:")
for index in range (len(final_array)):
    print (str(final_array[index]) + ", ", end = "")
    