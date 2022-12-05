# Problem Description:

# You are given an integer array prices where prices[i] is the 
# price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. 
# You can only hold at most one share of the stock at any time. 
# However, you can buy it then immediately sell it on the same day.

# Find and return the maximum profit you can achieve.

# EXAMPLE:
# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.

def getMaxProfit(prices):
    total_profit = 0
    l = len(prices)

    for i in range(1, l):
        # if price today is greater than price
        # yesterday
        if prices[i] > prices[i-1]:
            # total profit + difference in price (today) and (yesterday) 
            total_profit += prices[i] - prices[i-1]

    return total_profit

print(getMaxProfit([6,1,3,2,4,7]))


