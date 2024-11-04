from itertools import groupby

class Solution:
    def compressedString(self, word: str, ans = "") -> str:

        grps = [(k,len(list(g))) for k, g in groupby(word)]
        
        for k, cnt in grps:
            div, rem = divmod(cnt,9)
            ans+= ('9'+ k) * div
            if rem: ans+= str(rem)+k

        return ans