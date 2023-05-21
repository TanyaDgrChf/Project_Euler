#Problem 25
x = 1
y = 0 
i = 0
Sol = 0
for i in range (1,4000000000):
    if len(str(Sol)) < 1000:
        Sol += x
        x += y
        y = x - y
    else:
        print(str(i + 1)) #add 1 as the starting digit isn't included
        break