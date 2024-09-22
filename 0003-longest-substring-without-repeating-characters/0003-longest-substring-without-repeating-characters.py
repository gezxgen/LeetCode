class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        t = set()
        L = 0
        
        for R in range(n):
            if s[R] not in t:
                t.add(s[R])
                l = max(l, R - L + 1)
            else:
                while s[R] in t:
                    t.remove(s[L])
                    L += 1
                t.add(s[R])
        
        return l