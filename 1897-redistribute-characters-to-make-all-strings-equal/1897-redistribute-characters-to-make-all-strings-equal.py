class Solution:
    def makeEqual(self, ws: List[str]) -> bool:
        cnt, n = [0] * 26, len(ws)
        for w in ws:
            for c in w:
                cnt[ord(c) - 97] += 1
        for val in cnt:
            if val % n != 0:
                return False
        return True