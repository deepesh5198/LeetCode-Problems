# Problem Description:

# Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
# Output: "Sao Paulo" 
# Explanation: Starting at "London" city you will reach "Sao Paulo" city 
# which is the destination city. 
# Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

def destCity(paths):
    """
    :type paths: List[List[str]]
    :rtype: str
    """
    points = []
    if len(paths) == 1:
        return paths[0][1]
    
    else:
        for path in paths:
            for point in path:
                points.append(point)

        source_destination = [x for x in points if points.count(x) == 1]

        for i in source_destination:
            if points.index(i)%2 != 0:
                return i

print(destCity(paths = [["pYyNGfBYbm","wxAscRuzOl"],["kzwEQHfwce","pYyNGfBYbm"]]))