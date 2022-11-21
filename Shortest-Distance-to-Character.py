def shortestToChar(s, c):
    """
    :type s: str
    :type c: str
    :rtype: List[int]
    """
    l = len(s)
    res = []
    prev = s.find(c)
    for i in range(l):
        if i <= prev:
            res.append(abs(prev - i))

        else:
            if c in s[i:]:
                e = s[i:].find(c)
                e += i
        
                dist1 = abs(prev - i)
                dist2 = abs(e - i)
                
                if dist1 < dist2:
                    res.append(dist1)
                else:
                    res.append(dist2)
                    prev = e
            else:
                res.append(abs(prev - i))

    return res