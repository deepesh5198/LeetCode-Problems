# You want to maximize your profit by choosing a single day to buy 
# one stock and choosing a different day in the future to sell that stock.

# EXAMPLE:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy 
# before you sell.

# APPROACH:
# Sliding Window: Similar to Two pointer problem.
# Start Left at 0 and Right at 1
# if price at Day L is greater than price at Day R
# L = R
# and R = R+1

# else calculate profit and compare it with the current profit
# and update R
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) == 1:
        return 0

    l = 0
    r = 1
    max_profit = 0

    while r < len(prices):
        if prices[l] > prices[r]:
            l, r = r, r+1

        else:
            profit = prices[r] - prices[l]
            max_profit = max(profit, max_profit)
            r += 1

    return max_profit