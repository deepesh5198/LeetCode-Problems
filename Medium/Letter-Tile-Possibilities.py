# Problem Description:
# You have n  tiles, where each tile has one letter tiles[i] printed on it.

# Return the number of possible non-empty sequences of letters you can make 
# using the letters printed on those tiles.

# EXAMPLE:
# Input: tiles = "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

from itertools import permutations
from math import factorial

def numTilePossibilities(tiles) -> int:
    perm_set = set()
    l = len(tiles)

    for i in range(1, l+1):
        perm_set.update(permutations(tiles, i))

    return len(perm_set)

            




