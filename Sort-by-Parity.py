a = [2,0,1]
b = []
for i,num in enumerate(a):
    if num%2 == 0:
        e = a.pop(i)
        a.insert(0, e)


print(a)
