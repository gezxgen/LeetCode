class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stock, n = 0, 0
        for i in range(len(prices)-1):
            if prices[i+1] - prices[i] > 0:
                stock += prices[i+1] - prices[i]
        return stock