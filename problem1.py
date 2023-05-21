#Problem 1:
import math
#multiples of 5 = 5 + 10 + ... + 995 + 1000
#Sum of multiples of 5:
MOfFiveOne = 995 + 5
MOfFiveTwo = 995 / 5 * 1 / 2
MOfFive = int(MOfFiveOne * MOfFiveTwo)
#Sum of multiples of 3:
MOfThreeOne = 999 + 3
MOfThreeTwoPartOne = math.floor(999/3)
MOfThreeTwoPartTwo = MOfThreeTwoPartOne / 2
MOfThree = int(MOfThreeOne * MOfThreeTwoPartTwo)
#Repeat elimination:
n = 1000
i = 0
allnums = []
for i in range(n):
    if i % 15 == 0:
       allnums.append(i)
repeats = sum(allnums)
Answer = MOfThree + MOfFive - repeats
print(str(Answer))