string = str(input("Enter a string: "))

vowels = {"a", "e", "i", "o", "u"}

stringArray = []
vowelsSwapped = 0
newString = ""
seenVowels = set()

for frontChar in range (len(string)):
    
    if string[frontChar] in vowels:
        for backChar in range(len(string)-1, -1, -1):
            if string[backChar] in vowels and backChar not in seenVowels:
                newString += string[backChar]
                seenVowels.add(backChar)
                break
    else:
        newString += string[frontChar]
    
print (newString)

        
    

