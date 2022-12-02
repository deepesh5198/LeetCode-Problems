# Problem description:
# Given a directed acyclic graph, with n vertices numbered from 0 to n-1, 
# and an array edges where edges[i] = [fromi, toi] represents a directed edge 
# from node fromi to node toi.

# Find the smallest set of vertices from which all nodes in the graph are reachable. 
# It's guaranteed that a unique solution exists.

# Notice that you can return the vertices in any order.

# EXAMPLE:
# Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
# Output: [0,3]
# Explanation: It's not possible to reach all the nodes from a single vertex. 
# From 0 we can reach [0,1,2,5]. From 3 we can reach [3,4,2,5]. So we output [0,3].

def findSmallestSetOfVertices(n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: List[int]
    """
    # get all the unique destination nodes
    values = set([edge[1] for edge in edges])

    # store all the vertices in a list
    # that are not in values list
    res = [vertex for vertex in range(n) 
            if vertex not in values]
    
    # return the result
    return res