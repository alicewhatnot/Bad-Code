import this

userInput = str(input("Enter the string to be encoded: "))

if not userInput == "":
    currentCharacter = userInput[0]
    currentTotal = 0
    output = ""

    for character in userInput:
        if character == currentCharacter:
            currentTotal += 1
        else:
            output += f"{currentCharacter} {currentTotal} "
            currentCharacter = character
            currentTotal = 1

    output += f"{currentCharacter} {currentTotal}"
    print(output)
else:
    print("Empty input.")