def find_factors(number):
    count = 0
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            count += 1
            if number // i != i:
                count += 1

    return count


solved = False
a = 0
number = 0
while not solved:
    number += 1
    a += number
    print(a, find_factors(a))
    if find_factors(a) > 500:
        solved = True
        print(number)
    