def recursionSum(n):
    if n == 2:
        return 2
    if n % 2 == 0:
        return n + recursionSum(n-2)
    else:
        return recursionSum(n-1)

n = 11
print (recursionSum(n))
