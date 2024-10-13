class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        L, R = max(weights), sum(weights)
        mn, n = R, len(weights)
        
        @lru_cache(None)
        def possible(M: int):
            P = 0
            for _ in range(days):
                sm = 0
                while P < n and sm + weights[P] <= M:
                    sm += weights[P]
                    P += 1
            return P
        
        while L <= R:
            M = (L + R) // 2
            if possible(M) == n:
                R = M - 1
                mn = min(mn, M)
            else:
                L = M + 1
        return mn
