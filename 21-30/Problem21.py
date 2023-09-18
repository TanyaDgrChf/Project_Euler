import math
def divisor_sum(num):
    divisors = []
    sum = 0
    for i in range(1, math.floor(num / 2) + 1):
        if num % i == 0:
            divisors.append(i)
    for i in divisors:
        sum += i
    return sum


if __name__ == '__main__':
    total_sum = 0
    nums = [num for num in range(1, 10001)]
    tries = 0
    for i in nums:
        tries += 1
        j = divisor_sum(i)
        if i == divisor_sum(j):
            total_sum += (i + j)
        try:
            nums.remove(i)
            nums.remove(j)
        except:
            pass
    print(total_sum, tries)

