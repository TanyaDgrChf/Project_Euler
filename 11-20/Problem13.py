numbers = []
answer = 0
for i in range(100):
    g = input()
    numbers.append(int(g))

for i in numbers:
    answer += i

print(str(answer)[0:10])
