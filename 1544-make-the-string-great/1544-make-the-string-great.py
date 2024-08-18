class Solution:
    def makeGood(self, s: str) -> str:
        g = ""
        for c in s:
            if g and abs(ord(c) - ord(g[-1])) == 32:
                g = g[:-1]
            else:
                g += c
        return g