def diStringMatch(s):
    """
    :type s: str
    :rtype: List[int]
    """
    res = []
    choice = list(range(len(s)+1))
    r = 0
    for c in s:
        if c == "I":
            if choice:
                r = min(choice)
                res.append(r)
            
                choice.remove(r)
            else:
                return res

        else:
            if choice:
                r = max(choice)
                res.append(r)
            
                choice.remove(r)
            else:
                return res
    
    if choice:
        res.append(choice.pop())
    return res

print(diStringMatch(s = "DDDD"))