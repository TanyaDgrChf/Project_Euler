#Problem 6
sumOfSquare = 0
squareOfSums = 0
for i in range(1,101):
    sumOfSquare += i**2
    squareOfSums += i

answer = squareOfSums**2 - sumOfSquare

print(answer)
    