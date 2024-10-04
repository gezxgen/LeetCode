class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window, s1 = len(s1), Counter(s1)
        
        for i in range(len(s2)-window+1):
            s = Counter(s2[i:i+window])
            if s == s1:
                return True
            
        return False