n = 9
def num_base(n, b):
    if n == 1:
        return "1"

    if n == 0:
        return "0"

    else:
        d = n // b
        r = n%b

        return num_base(d, b) + str(r)

for b in range(2, n-1):
    num = num_base(n, b)

    if num != num[::-1]:
        print(False)
        break

# print(True)
