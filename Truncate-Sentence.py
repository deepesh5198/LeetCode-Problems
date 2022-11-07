# Problem Description:
# Input: s = "Hello how are you Contestant", k = 4
# Output: "Hello how are you"
# Explanation:
# The words in s are ["Hello", "how" "are", "you", "Contestant"].
# The first 4 words are ["Hello", "how", "are", "you"].
# Hence, you should return "Hello how are you".

def truncateSentence(s, k) -> str:
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    s = s.split(" ")
    return " ".join(word for word in s[:k])

s = {1,2,3}
s.inter
print(list(s))