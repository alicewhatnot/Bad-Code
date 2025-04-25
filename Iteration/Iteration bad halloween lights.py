import time
from random import randint

while True:
    randomTime = randint(100,1000)
    time.sleep(randomTime/1000)
    print ("-----")
    randomTime = randint(10,100)
    time.sleep(randomTime/1000)
    print ("*****")

    