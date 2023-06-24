def collatz(initial):
    return collatz_rec(initial, 0)
def collatz_rec(initial, count):
    if initial % 2 == 0:
        initial = initial / 2
        count += 1
        return collatz_rec(initial, count)
    elif initial == 1:
        return count
    else:
        initial = (initial * 3) + 1
        count += 1
        return collatz_rec(initial, count)
starting_number = 0
highest = 0
for i in range(1, 999999):
    g = collatz(i)
    if g > highest:
        highest = g
        starting_number = i
print(starting_number)