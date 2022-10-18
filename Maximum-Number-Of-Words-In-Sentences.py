#A sentence is a list of words that are separated by a single space with
# no leading or trailing spaces.

# You are given an array of strings sentences, where each sentences[i] 
# represents a single sentence.

# Return the maximum number of words that appear in a single sentence.

#EXAMPLE:
# Input: sentences = ["alice and bob love leetcode", "i think so too",
#                     "this is great thanks very much"]
# Output: 6

# Explanation: 
# - The first sentence, "alice and bob love leetcode", has 5 words in total.
# - The second sentence, "i think so too", has 4 words in total.
# - The third sentence, "this is great thanks very much", has 6 words in total.

# Thus, the maximum number of words in a single sentence comes from the third 
# sentence, which has 6 words.


def maximumNumOfWords(sentences):
    max_words = 0
    max_words = 0
    for sentence in sentences:
        num_of_words = len(sentence.split())
        if max_words < num_of_words: 
            max_words = num_of_words

    return max_words

print(maximumNumOfWords(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))