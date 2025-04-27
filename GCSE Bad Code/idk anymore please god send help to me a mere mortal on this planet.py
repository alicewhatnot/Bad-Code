import statistics
examResults = [63,92,84,57,72,94,63]
candidates = ["Diya","Ali","Charles","Eric","Hanna","Gabriel","Delores"]
print ("the highest result was",max(examResults))
print ("the lowest result was",min(examResults))
print ("the mean result was",statistics.mean(examResults))
candidates.sort()
for i in range (0,len(candidates)):
    print ("Candidate",i+1,":",candidates[i])
    

