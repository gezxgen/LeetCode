class Solution:
    def arrangeCoins(self, n: int) -> int:
        cnt, i = 0, 1
        
        while i <= n:
            n -= i
            cnt += 1
            i += 1
        
        return cnt