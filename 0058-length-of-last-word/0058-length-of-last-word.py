class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word: str = s.strip().split(" ")[-1]
        return len(word)