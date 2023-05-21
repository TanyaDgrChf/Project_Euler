#Problem 4
import math
reverseSection = ''
answer = 0
for a in range(100, 999):
    for b in range(100, 999):
        product = a * b
        g = math.floor(len(str(product)) / 2)
        firstFewNumbers = str(product)[0:g]
        lastFewNumbers = str(product)[0 - g:]
        reversedLastFewNumbers = lastFewNumbers[::-1]
        if int(firstFewNumbers) == int(reversedLastFewNumbers) and product > answer:
            answer = product
print(answer)