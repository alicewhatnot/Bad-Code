#Time Taken: 18.25
#Marks Worth: 12

amount = int(input("Enter the number of numbers to be entered: "))
numbers = []
count = [0,0,0,0,0,0,0,0,0,0]

for i in range (amount):
    numbers.append(int(input(f"Enter number {i+1}: ")))

for i in range (10):
    for j in range (len(numbers)):
        if numbers[j] == i:
            count[i] += 1

modal = max(count)

count.remove(modal)
if modal in count:
    print ("Data is multimodal")
else:
    print (f"Mode is {modal}")