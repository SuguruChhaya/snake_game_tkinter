a ='hi'
b = a
a = 'yeet'
print(a, b)

a = [[1,2]]
a[0].remove(1)
print(a)

for i in range(0,2):
    #*Good thing is that 'break' only breaks from the nearest for loop.
    for c in range(0, 2):
        print(i)
        print(c)
        if c == 1:
            break
e = 3
d = [[e]]
e = 100
d.append(e)
print(d)

#*The mutation that occurs
f = [1,2]
g = [f]
print(g)
g[0].append(3)
print(g)
print(f)
