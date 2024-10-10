class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time, mx = 0, 0
        for i in range(len(colors)):
            if i != 0 and colors[i] != colors[i - 1]:
                mx = 0
            time += min(neededTime[i], mx)
            mx = max(mx, neededTime[i])
        return time