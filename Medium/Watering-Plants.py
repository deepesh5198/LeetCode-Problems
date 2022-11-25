# Problem Description:

# Input: plants = [2,2,3,3], capacity = 5
# Output: 14
# Explanation: Start at the river with a full watering can:
# - Walk to plant 0 (1 step) and water it. Watering can has 3 units of water.
# - Walk to plant 1 (1 step) and water it. Watering can has 1 unit of water.
# - Since you cannot completely water plant 2, walk back to the river to refill (2 steps).
# - Walk to plant 2 (3 steps) and water it. Watering can has 2 units of water.
# - Since you cannot completely water plant 3, walk back to the river to refill (3 steps).
# - Walk to plant 3 (4 steps) and water it.
# Steps needed = 1 + 1 + 2 + 3 + 3 + 4 = 14.

def wateringPlants(plants, capacity):
    """
    :type plants: List[int]
    :type capacity: int
    :rtype: int
    """
    # current capacity == initial capacity
    cur_capacity = capacity

    # initialize steps to 0
    steps = 0

    # initilize i and j at zero
    i = 0
    j = 0
    # get the length of array
    l = len(plants)

    # start while loop
    while i != l:
        # if cur_capacity <= the water the
        # plant at ith position need
        if plants[i] <= cur_capacity:
            # check if we got back to refill water
            # if not
            if j != i:
                steps +=1
                cur_capacity -=plants[i]
                i +=1

            # if yes
            else:
                # add the number of steps to reach position
                # we left to get water + the step to water that plant
                steps +=i + 1
                cur_capacity -=plants[i]
                i += 1

        # go to refill the can
        else:
            # set j == current position
            j = i
            
            # steps to reach the river
            steps += i

            # fill the can
            cur_capacity = capacity

    # return total steps
    return steps

print(wateringPlants(plants = [2], capacity = 1))