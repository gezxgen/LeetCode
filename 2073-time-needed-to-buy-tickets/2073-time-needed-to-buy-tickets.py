class Solution:
    def timeRequiredToBuy(self, tks: List[int], k: int) -> int:
        tot = 0
        for i in range(len(tks)):
            if i <= k: tot += min(tks[i], tks[k])
            else: tot += min(tks[i], tks[k] - 1)
        return tot