# Problem Statement:
# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]
# Explanation: "mee" matches the pattern because there is a permutation 
# {a -> m, b -> e, ...}. 
# "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a 
# permutation, since a and b map to the same letter.

def findAndReplacePattern(words, pattern):
    """
    :type words: List[str]
    :type pattern: str
    :rtype: List[str]
    """
    def match(word):
        map1 = {}
        map2 = {}
    
        for w, p in zip(word, pattern):
            if w not in map1:
                map1[w] = p
                
            if p not in map2:
                map2[p] = w

            if (map1[w], map2[p]) != (p, w):
                return False

        return True
    return filter(match, words)