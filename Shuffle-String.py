#Problem Description:
# You are given a string s and an integer array indices of the same length.
# The string s will be shuffled such that the character at the ith position
# moves to indices[i] in the shuffled string.

# Return the shuffled string.

#EXAMPLE:
#Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"
# Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

def shuffleString(s:str, indices:list) ->str:
    """
    this function returns a shuffled string
    """

    #create a mapping of "index : char"
    #this index act as new index 
    mapping = {key:value for value,key in zip(s, indices)}
    
    #join the chars from mapping
    #with ordered index "01234567..."    
    result_string = "".join(mapping[i] for i in\
                                range(len(mapping))) 
        
    return result_string