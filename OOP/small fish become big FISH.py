def feed (state, size):
    size = size + 1
    print ("Fish fed")
    if size == 9:
        state = "FISH"
    return state, size

thisFishState = "Fish"
thisFishSize = 1
print (f"{thisFishState} is of size {thisFishSize}")
while thisFishState != "FISH":
    thisFishState, thisFishSize = feed(thisFishState, thisFishSize)
print (f"It is now a big {thisFishState}")