class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stock, n = 0, 0
        for i in range(len(prices)-1):
            n = prices[i+1] - prices[i]
            if n > 0: stock += n
        return stock