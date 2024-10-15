class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # for search have a function to call
        def possible(M):
            return sum(ceil(pile / M) for pile in piles) <= h
        
        # set L, R as range
        L, R = 1, max(piles)
        
        # binary search the range
        while L < R:
            M = (L + R) // 2
            if possible(M):
                R = M
            else:
                L = M + 1
        
        return M if possible(M) else M + 1