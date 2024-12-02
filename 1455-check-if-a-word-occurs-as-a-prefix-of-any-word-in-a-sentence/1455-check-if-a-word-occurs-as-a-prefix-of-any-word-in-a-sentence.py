class Solution:
    def isPrefixOfWord(self, s: str, t: str) -> int:
        return -1 if (m:=(s:=' '+s).find(' '+t))==-1 else 1+s[:m].count(' ')