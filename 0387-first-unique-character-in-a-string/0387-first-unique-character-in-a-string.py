class Solution:
    def firstUniqChar(self, s: str) -> int:
        # count in HashMap
        mp: dict[str, int] = {}
        for char in s:
            mp[char] = mp.get(char, 0) + 1
        
        # return first with value 1
        for i in range(len(s)):
            if mp[s[i]] == 1:
                return i
        return -1