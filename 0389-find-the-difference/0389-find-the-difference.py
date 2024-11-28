class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # hash s and t
        smp = {}
        for c in s:
            smp[c] = smp.get(c, 0) + 1
        
        tmp = {}
        for c in t:
            tmp[c] = tmp.get(c, 0) + 1
        
        # find the difference
        for c in tmp.keys():
            if tmp[c] != smp.get(c, 0):
                return c