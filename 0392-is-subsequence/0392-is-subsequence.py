class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        L, R = 0, len(s)
        
        if not s:
            return True
        
        for i in range(len(t)):
            if t[i] == s[L]:
                L += 1
                if L == R:
                    return True
        return False