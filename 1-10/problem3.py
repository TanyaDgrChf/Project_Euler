#Problem #3
import math
number = int(600851475143)
set = []
largestFactorFound = False
def findNextFactor(x1): #Find the next largest factor
    factorFound = False #Flag variable to check whether a factor has been found
    for a in range(2, int(x1)-1):
        if x1 % a == 0: #check if a is a factor of x1
            return(a)
            factorFound = True #prevents the second if condition from being ran
            break
    if not factorFound:
        return(600851475144)
while not largestFactorFound:
    if findNextFactor(number) != 600851475144:
        number = number / findNextFactor(number)
    else:
        print(number)
        largestFactorFound = True