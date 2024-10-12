class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        L, R = 0, num
        
        while L <= R:
            M = (L + R) // 2
            n = M ** 2
            
            if n < num:
                L = M + 1
            elif n > num:
                R = M - 1
            else:
                return True
        
        return False