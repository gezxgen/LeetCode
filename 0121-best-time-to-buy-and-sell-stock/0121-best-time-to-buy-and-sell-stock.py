class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tot: int = 0
        mx: int = prices[-1]
        
        for i in range(len(prices)-1, -1, -1):
            # go through and track max on right
            # also save the best time
            # if at the left end, return best time
            if prices[i] > mx:
                mx = prices[i]
            elif (mx - prices[i]) > tot:
                tot = mx - prices[i]
        return tot