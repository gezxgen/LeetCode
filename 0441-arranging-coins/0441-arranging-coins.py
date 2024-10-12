class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((pow(1 + 8 * n, 0.5) - 1) / 2)