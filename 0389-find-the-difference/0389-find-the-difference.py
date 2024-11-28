class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # hash
        mp = {}
        for i in range(len(s)):
            mp[t[i]] =  mp.get(t[i], 0) + 1
            mp[s[i]] =  mp.get(s[i], 0) - 1
        mp[t[-1]] = mp.get(t[-1], 0) + 1
        
        # find the difference
        return next(key for key, value in mp.items() if value == 1)