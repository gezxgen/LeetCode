class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        L = 0
        
        if not s:
            return True
        
        for i in range(len(t)):
            if t[i] == s[L]:
                L += 1
                if L == len(s):
                    return True
        return False