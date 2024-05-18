class Solution:
    def reverseString(self, s: List[str]) -> None:
        l = 0
        r = len(s) - 1
        m = ""
        
        while l < r:
            m = s[l]
            s[l] = s[r] 
            s[r] = m
            
            l += 1
            r -= 1

        