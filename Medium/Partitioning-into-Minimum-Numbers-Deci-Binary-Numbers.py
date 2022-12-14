# Problem Description:
# Return minimum number of Deci-binary numbers to sum up to the given number.

def returnListOfDeciBinary(n):
    res = []
    count = 0
    while n != "0"*len(n):
        
        s = "".join("1" if c>'0' else '0' for c in n)
        
        res.append(s)

        n = str(int(n) - int(s))
        
        count +=1

    return res

# print(returnListOfDeciBinary('34'))

def returnListOfDeciBinary_recursive(n, res):
    if n == "0"*len(n):
        return res

    else:
        s = "".join("1" if c>"0" else "0" for c in n)

        n = str(int(n) - int(s))
        res.append(s)
        return returnListOfDeciBinary_recursive(n, res)

print(returnListOfDeciBinary_recursive("2451", []))
    