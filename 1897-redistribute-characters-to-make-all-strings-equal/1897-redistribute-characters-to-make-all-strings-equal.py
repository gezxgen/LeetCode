class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        mp, n = {}, len(words)
        
        for word in words:
            for char in word:
                mp[char] = mp.get(char, 0) + 1
        
        for char in mp:
            if mp[char] % n != 0:
                return False
        
        return True