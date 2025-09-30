letter = str(input("Enter a lowercase letter: "))
largest = letter
smallest = letter
for i in range (1,4):
    letter = str(input("Enter a lowercase letter: "))
    if letter > largest:
        largest = letter
    elif letter < smallest:
        smallest = letter
print ("The largest was: ",largest)
print ("The smallest was: ",smallest)
    