# 9 COMBINATIONS WITH 9 PERMUTATIONS TOOK 47 MINUTES 30 SECONDS

#-----TO DO------
# LIST NUMBER OF MAGIC SQUARES FOUND AND THEIR NUMBERS NOT JUST FLAG IF ONE FOUND AND LIST LAST NUMBER SET FOUND
# FIND SOME WAY OF ITERATING UPWARDS INSTEAD OF DOWNWARDS AS TO BE ABLE TO COMPUTE PARRALEL / SEPERATE SESSIONS
# FIND MY OWN HUGE MAGIC SQUARE
# ATTEMPT TO FIND A NON-PARKER MAGIC SQUARE OF SQUARES

import itertools

foundOne = "FALSE"
numbers = list(range(1, 10))
combinations_of_9 = itertools.combinations(numbers, 9)
for comb in combinations_of_9:
    permutations = itertools.permutations(comb)
    for perm in permutations:
#        if foundOne == "TRUE":
#           break
        a, b, c, d, e, f, g, h, i = perm
        print (f"a={a}, b={b}, c={c}, d={d}, e={e}, f={f}, g={g}, h={h}, i={i}")
        work = "TRUE"
        magicNumber = (a+b+c)
        if magicNumber != (d+e+f):
            work = "FALSE"
        if magicNumber != (g+h+i):
            work = "FALSE"
        if magicNumber != (a+d+g):
            work = "FALSE"
        if magicNumber != (b+e+h):
            work = "FALSE"
        if magicNumber != (c+f+i):
            work = "FALSE"
        if magicNumber != (a+e+i):
            work = "FALSE"
        if magicNumber != (g+e+c):
            work = "FALSE"
        if work == "TRUE":
            foundOne = "TRUE"
            numberA = a
            numberB = b
            numberC = c
            numberD = d
            numberE = e
            numberF = f
            numberG = g
            numberH = h
            numberI = i
        print (work)

        
