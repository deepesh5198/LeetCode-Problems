# Problem Description:

# Input: logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5
# Output: [0,2,0,0,0]
# Explanation:
# The user with ID=0 performed actions at minutes 5, 2, and 5 again. Hence,
# they have a UAM of 2 (minute 5 is only counted once).
# The user with ID=1 performed actions at minutes 2 and 3. Hence, they have a UAM of 2.
# Since both users have a UAM of 2, answer[2] is 2, and the remaining answer[j] 
# values are 0.

from collections import defaultdict
def findingUsersActiveMinutes(logs, k):
    """
    :type logs: List[List[int]]
    :type k: int
    :rtype: List[int]
    """
    # create a list of zeros of size k
    answer = [0]*k

    # create a default dictionary of sets
    dd = defaultdict(set)

    # for each log
    for l in logs:
        # default dict: key = l[0], 
        # value = set().add(l[1])
        dd[l[0]].add(l[1])

    # for id in default dict
    for id in dd:
        # add 1 at location (len(dd[id]) - 1) in answer
        answer[len(dd[id])-1] +=1
        
    return answer