# Problem Description:
# You are given an integer array prices where prices[i] is the price of the ith item in a shop.

# There is a special discount for items in the shop. If you buy the ith item, then you will 
# receive a discount equivalent to prices[j] where j is the minimum index 
# such that j > i and prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.

# Return an integer array answer where answer[i] is the final price you will pay for 
# the ith item of the shop, considering the special discount.

# EXAMPLE:
# Input: prices = [8,4,6,2,3]
# Output: [4,2,4,2,3]
# Explanation: 
# For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.
# For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.
# For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.
# For items 3 and 4 you will not receive any discount at all.

def finalPrices(prices):
    """
    :type prices: List[int]
    :rtype: List[int]
    """
    l = len(prices)
    for i, n in enumerate(prices):
        if i != l-1:
            for j in prices[i+1:]:
                if j <= n:
                    print(j)
                    break
                else:
                    j = 0
            prices[i] -= j
            
    return prices

print(finalPrices(prices = [8,7,4,2,8,1,7,7,10,1]))