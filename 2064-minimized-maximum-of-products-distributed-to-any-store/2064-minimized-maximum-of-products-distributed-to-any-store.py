class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # binary search the wanted value
        L, R = ceil(sum(quantities) / n), max(quantities)
        while L <= R:
            M = (L + R) // 2
            if n >= sum([ceil(num / M) for num in quantities]):
                R = M - 1
            else:
                L = M + 1
        return M if n >= sum([ceil(num / M) for num in quantities]) else M + 1