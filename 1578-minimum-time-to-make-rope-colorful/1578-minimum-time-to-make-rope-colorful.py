class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        tot, i, j, n = 0, 0, 0, len(neededTime)
        while i < n and j < n:
            cur = 0
            mx = 0
            while j < n and colors[i] == colors[j]:
                cur += neededTime[j]
                mx = max(mx, neededTime[j])
                j += 1
            tot += cur - mx
            i = j
        return tot