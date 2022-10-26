# Problem Description:
# Given a sentence with words containing numbers, sort it.

# EXAMPLE:
# Input: s = "is2 sentence4 This1 a3"
# Output: "This is a sentence"
# Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.

def sortTheSentence(sentence):
    f = lambda x: x[-1]
    sentence = sorted(sentence.split(), key= f )
    
    return " ".join(word.replace(word[-1], "") for word in sentence)

print(sortTheSentence(sentence= "is2 sentence4 This1 a3"))