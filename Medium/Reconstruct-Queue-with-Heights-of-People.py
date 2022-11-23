# You are given an array of people, people, which are the attributes of some 
# people in a queue (not necessarily in order). Each people[i] = [hi, ki] 
# represents the ith person of height hi with exactly ki other people in 
# front who have a height greater than or equal to hi.

# Reconstruct and return the queue that is represented by the input array people. 
# The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] 
# is the attributes of the jth person in the queue (queue[0] is the person at 
# the front of the queue).

# Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
# Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]

def reconstructQueue(people):
    """
    :type people: List[List[int]]
    :rtype: List[List[int]]
    """
    # initialize an empty list
    queue = []

    # sort the people list in 
    # descending order
    # if heights of 2 people are same,
    # then sort them according to their
    # p[1] value in ascending order
    # example: [7,1], [7,0] ==> [7,0], [7,1] 
    people.sort(key= lambda x: (-x[0], x[1]))

    for p in people:
        queue.insert(p[1], p)
    
    return queue