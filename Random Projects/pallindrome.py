pallindrome = str(input("Enter a pallindrome: "))
works = True
for i in range(len(pallindrome)):
    if pallindrome[-i-1]!=pallindrome[i]:
        works = False
if works == False:
    print ("That isnt a pallindrome.")
else:
    print ("That is a pallindrome!")