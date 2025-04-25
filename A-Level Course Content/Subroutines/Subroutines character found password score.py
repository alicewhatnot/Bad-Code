lowercase = [chr(letter) for letter in range(97,123)]
uppercase = [chr(letter) for letter in range(65,91)]
numbers = [chr(letter) for letter in range(48,58)]
characters = [chr(letter) for letter in range(33,48)]+[chr(letter) for letter in range(58,65)]+[chr(letter) for letter in range(91,97)]+[chr(letter) for letter in range(124,127)]

def checkLowercase(password):
    score = 0
    lowerFound = False
    for item in password:
        if item in lowercase:
            score = score + 5
            lowerFound = True
    return score,lowerFound

def checkUppercase(password):
    score = 0
    upperFound = False
    for item in password:
        if item in lowercase:
            score = score + 5
            upperFound = True
    return score,lowerFound

def checkNumbers(password):
    score = 0
    numberFound = False
    for item in password:
        if item in lowercase:
            score = score + 10
            lowerFound = True
    return score,numberFound

def checkCharacters(password):
    score = 0
    characterFound = False
    for item in password:
        if item in lowercase:
            score = score + 10
            lowerFound = True
    return score,characterFound

totalScore = 0
score = 0
lowerFound = False
upperFound = False
numberFound = False
characterFound = False
password = input("Enter a password")
score,lowerFound = checkLowercase(password)
totalScore = totalScore + score
score,upperFound = checkUppercase(password)
totalScore = totalScore + score
score,numberFound = checkNumbers(password)
totalScore = totalScore + score
score,characterFound = checkCharacters(password)
totalScore = totalScore + score
print (f"Your score was:{totalScore}")
print (lowerFound)
print (upperFound)
print (numberFound)
print (characterFound)

