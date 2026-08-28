import random

def flipUntilHeadMajority():
    totalflips = 0
    heads = 0
    tails = 0
    while heads <= tails:
        coin = random.randint(0,1)
        totalflips += 1
        if coin == 1:
            heads += 1
        else:
            tails += 1
    return (heads/totalflips)

attempts = 0
runningRatio = 0
while True:
    attempts += 1
    newRatio = flipUntilHeadMajority()
    runningRatio = (runningRatio*(attempts-1) + newRatio)/attempts
    print (f"π/4 ≈ {runningRatio}")
    print (f"π ≈ {runningRatio*4}")
    print (f"Number of attempts: {attempts}")