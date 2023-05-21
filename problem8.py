#Problem 8
a = 10**99
g = 1
z = 0
for i in range(1, 987):
    for j in range(1,14):
        g = g * int(str(a)[i + j])
    if g > z:
        z = g
        g = 1
    else:
        g = 1
print(z)    