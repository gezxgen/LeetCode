class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # hash
        p = 0
        for i in range(len(s)):
            p += ord(t[i]) - ord(s[i])
        
        # find the difference
        return chr(p + ord(t[-1]))