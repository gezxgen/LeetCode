class Solution:
    def arrangeCoins(self, n: int) -> int:
        @lru_cache(None)
        def meth(n):
            cnt, i = 0, 1
        
            while i <= n:
                n -= i
                cnt += 1
                i += 1

            return cnt
        return meth(n)