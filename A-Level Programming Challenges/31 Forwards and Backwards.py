def checkPalindrome(word):
    #Creating arrays to split the word in half
    firstHalf = []
    secondHalf = []
    
    #Turn the word into a list for string manipulation
    wordList = list(word)

    #Removing spaces if included e.g. race car
    for i in range (len(wordList)-1):
        if wordList[i] == " ":
            wordList.pop(i)
    
    #Removing the middle letter if the word is odd
    if (len(wordList)%2 != 0):
        middle = (int(len(wordList)/2))
        wordList.pop(middle)            
    
    #Splitting the word into two arrays, second is reverse order
    for i in range (int(len(wordList)/2)):
        firstHalf.append(wordList[i])
        
    for i in range ((len(wordList)-1),(int(len(wordList)/2)-1),-1):
        secondHalf.append(wordList[i])
    
    #Outputting based on comparing the halves
    if firstHalf == secondHalf:
        print (f"{word} is a palindrome.")
    else:
        print (f"{word} is not a palindrome.")
    
#MAIN CODE
word = str(input("Enter a word. "))
checkPalindrome(word)

