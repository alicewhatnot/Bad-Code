# Scramble

word1 = str(input("Enter the first word: "))
word2 = str(input("Enter the second word: "))

word1Array = []
word2Array = []
matchesMade = 0

for letter in word1:
    word1Array.append(letter)

for letter in word2:
    word2Array.append(letter)

for letter in word1Array:
    for letterInWord2 in word2Array:
        if letter == letterInWord2:
            matchesMade += 1
            word2Array.remove(letterInWord2)
            print(f"Letter {letter} found.")
            break

if matchesMade == len(word1):
    print(f"{word1} can be created from the letters of {word2}.")
else:
    print(f"{word1} cannot be created from the letters of {word2}.")

