class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        L, R = max(weights), sum(weights)
        mn, n = R, len(weights)
        
        while L <= R:
            M = (L + R) // 2
            
            P = 0
            for _ in range(days):
                sm = 0
                while P < n and sm + weights[P] <= M:
                    sm += weights[P]
                    P += 1
                    
            if P == n:
                R = M - 1
                mn = min(mn, M)
            else:
                L = M + 1
        
        return mn
