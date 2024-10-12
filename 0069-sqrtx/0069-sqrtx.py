class Solution:
    def mySqrt(self, x: int) -> int:
        L, R = 0, x
        
        while L <= R:
            M = (L + R) // 2
            n = ceil(M ** 2)
        
            if n < x:
                L = M + 1
            elif n > x:
                R = M - 1
            else:
                return M
        
        return R