def fact(n):
    if n <= 1:
        return 1

    else:
        return n*fact(n-1)

pascal = []
n = 5

for i in range(n):
    sub_list = []
    for j in range(i+1):
        nCr = fact(i)//(fact(i-j)*fact(j))
        sub_list.append(nCr)
    pascal.append(sub_list)

print(pascal)