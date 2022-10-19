# Problem Description:
# Given the array nums consisting of 2n elements in the 
# form [x1,x2,...,xn,y1,y2,...,yn].

# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

#EXAMPLE:
# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7] 
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

def shuffleArray(nums, n):
    #break the array in 2 parts
        #A: first half
        #B: second half
        A = nums[:n]
        B = nums[n:]
        
        #initialize an empty list C
        C = []

        for i, j in zip(A,B):
            #append element from A to C
            C.append(i)
            #append element from B to C
            C.append(j)

        return C