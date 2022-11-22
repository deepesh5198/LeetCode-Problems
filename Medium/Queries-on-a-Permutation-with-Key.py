# Problem Description
# Given the array queries of positive integers between 1 and m, 
# you have to process all queries[i] (from i=0 to i=queries.length-1) 
# according to the following rules:

# In the beginning, you have the permutation P=[1,2,3,...,m].
# For the current i, find the position of queries[i] in the 
# permutation P (indexing from 0) and then move this at the 
# beginning of the permutation P. Notice that the position of 
# queries[i] in P is the result for queries[i].

# Return an array containing the result for the given queries.

def processQueries(queries, m):
    """
    :type queries: List[int]
    :type m: int
    :rtype: List[int]
    """
    # initializing Permutation list
    P = list(range(1,m+1))

    # initialize an empty list for outputs
    res = []

    # going through each queries
    for q in queries:
        # get the position of the query point in
        # permutation list
        pos = P.index(q)

        # append the position into the result list
        res.append(pos)

        # pop the element from Permutation at the position
        # and insert it at the beginning 
        P.insert(0, P.pop(pos))
    
    # return the result list
    return res

print(processQueries(queries = [7,5,5,8,3], m = 8))