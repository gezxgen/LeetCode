class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        w = s.strip().split()
        return len(w[-1])