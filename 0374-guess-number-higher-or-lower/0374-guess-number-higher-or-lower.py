# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        L, R = 0, n
        
        while True:
            M = (L + R) // 2
            n = guess(M)
            if n == 1:
                L = M+1
            elif n == -1:
                R = M-1
            else:
                return M