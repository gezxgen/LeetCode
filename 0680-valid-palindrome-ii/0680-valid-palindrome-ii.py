class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0                           # create variables
        r = len(s) - 1
                
        while l < r:                    # check if palindrome
            if s[l] != s[r]:
                L = s[l + 1:r + 1]      # check if it can be fixed
                R = s[l:r]
                return (R == R[::-1]) or (L == L[::-1])
                
            l += 1
            r -= 1
            
            
        return True