class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        if len(prices) == 0: return 0

        for i in range(len(prices)):
            curr_price = prices[i]
            if curr_price < min_price:
                min_price = curr_price
            profit = curr_price - min_price
            if profit > max_profit:
                max_profit = profit
        return max_profit
