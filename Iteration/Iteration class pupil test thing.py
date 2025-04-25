testScoreTotal = 0
testScore1Total = 0
testScore2Total = 0
testScore3Total = 0
for i in range (1,31):
    print ("Enter the test scores for pupil",i)
    testScore1 = float(input("Test 1: "))
    testScore1Total = testScore1Total + testScore1
    testScore2 = float(input("Test 2: "))
    testScore2Total = testScore2Total + testScore2
    testScore3 = float(input("Test 3: "))
    testScore3Total = testScore3Total + testScore3
    testScoreTotal = testScoreTotal + testScore1 + testScore2 + testScore3
print ("The average test score was: ",testScoreTotal/30)
print ("The average test 1 score was:",testScore1Total/30)
print ("The average test 2 score was:",testScore2Total/30)
print ("The average test 3 score was:",testScore3Total/30)
