class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx = 0
        start = prices[0]
        len1 = len(prices)
        for i in range(0 , len1):
            if start < prices[i]: 
                mx += prices[i] - start
            start = prices[i]
        return mx