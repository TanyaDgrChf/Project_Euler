#Problem 2:
x = 1
y = 1 
i = []
Sol = 0
for i in range (1,40000):
    if x < 4000000 and x % 2 == 0:
        Sol += x
        x += y
        y = x - y
    elif x < 4000000 and x % 2 > 0:
        x += y
        y = x - y
    else:
        i += Sol
print(str(Sol))
