import time
list = []

time1 = time.time()
for i in range (99999):
    list = list + [i]
time2 = time.time()
for i in range (99999):
    list.append(i)
time3 = time.time()

print ((time2-time1)*1000)
print ((time3-time2)*1000)