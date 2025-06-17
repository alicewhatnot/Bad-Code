import time

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1    
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci2(n):
    fibNumbers = [0,1]  #list of first two Fibonacci numbers
# now append the sum of the two previous numbers to the list    
    for i in range(2, n+1):
        fibNumbers.append(fibNumbers[i-1] +fibNumbers[i-2])
    return fibNumbers[n]

n = 30
time1 = time.time()
print (fibonacci(n))
time2 = time.time()
print (fibonacci2(n))
time3 = time.time()
print ("---------")
print ((time2-time1)*1000)
print ((time3-time2)*1000)