# 121. Best Time to Buy and Sell Stock
# Easy

# 11696

# 442

# Add to List

# Share
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104







# Success
# Details 
# Runtime: 1144 ms, faster than 46.78% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 25.1 MB, less than 54.59% of Python3 online submissions for Best Time to Buy and Sell Stock.



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price =max(prices)
        max_price = 0
        
        for i in range(len(prices)):
            min_price = min(min_price,prices[i])
            max_price = max(max_price, prices[i] - min_price)
        
        return max_price
  
  
#   Success
# Details 
# Runtime: 944 ms, faster than 93.74% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 25.2 MB, less than 11.83% of Python3 online submissions for Best Time to Buy and Sell Stock.

      
      
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price =max(prices)
        max_price = 0
        
        for i in range(len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            elif max_price < prices[i] - min_price:
                max_price = prices[i] - min_price
        
        return max_price
