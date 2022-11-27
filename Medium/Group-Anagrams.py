# Problem Description:
# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a 
# different word or phrase, typically using all the original letters exactly once.

# EXAMPLE:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

from collections import defaultdict, Counter

# THIS IS A VERY VERY SLOW APPROACH
def groupAnagramsV1(strs):
    res = []
    while strs:
        res.append([strs.pop(0)])
        for s2 in strs[:]:
            chars = set(s2)
            if len(res[-1][0]) == len(s2)\
                and [s2.count(c) for c in chars]\
                == [res[-1][0].count(c) for c in chars]\
                and (set(res[-1][0]) == chars):
                res[-1].append(s2)
                strs.remove(s2)
    return res

# THIS IS FAST APPROACH
def groupAnagramsV2(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    groups = defaultdict(list)
    for s in strs:
        groups[frozenset(Counter(s).items())].append(s)
        
    return groups.values()