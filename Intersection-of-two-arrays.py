#Problem Description:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

def intersection(nums1, nums2):
    
    nums1 = set(nums1)
    nums2 = set(nums2)
    
    return list(nums1.intersection(nums2))