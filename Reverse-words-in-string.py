#Problem Description:
# Given a string "s", reverse the order of characters in each word within
# a sentence while still preserving whitespace and initial word order.

#EXAMPLE
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

def reverseWords(stringg):
    return " ".join(word[::-1] for word in stringg.split())


print(reverseWords("Let's take LeetCode contest"))