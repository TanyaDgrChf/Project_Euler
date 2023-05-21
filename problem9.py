#Problem 9
for c in range(1, 800):
    for b in range(1, c):
        for a in range(1, c):
            if a + b + c == 1000:
                if a**2 + b**2 == c**2:
                    print(a * b * c)