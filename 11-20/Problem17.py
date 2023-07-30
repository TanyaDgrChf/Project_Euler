import inflect
inf = inflect.engine()
ans = 0
for i in range(1, 1000 + 1):
    a = inf.number_to_words(i)
    for char in a:
        if char.isalpha():
            ans += 1
print(ans)