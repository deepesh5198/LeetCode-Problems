def findTheWinner(n: int, k: int) -> int:
    # make a list of friends
    friends = list(range(1, n+1))

    # initialize i and j as 0
    i = 0
    j = 0

    # run this loop until
    # n == 1
    while n != 1:
        
        # count value of i and j
        while i < k-1:
            i +=1
            j +=1
            
            # if j crosses value of n
            # make it zero
            if j >= n:
                j = 0

        # if j == n-1
        if j == n - 1:
            friends.pop(j)
            n -= 1
            j = 0
            i = 0
            continue

        # if j is smaller than n    
        if j < n:
            friends.pop(j)
            n -= 1
            i = 0

    return friends[0]

print(findTheWinner(500,50))

