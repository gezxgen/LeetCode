class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not g or not s:
            return 0
        
        l1, l2 = len(g), len(s)
        g.sort()
        s.sort()
        j = 0
        cnt = 0
        
        for i in range(l1):
            while j < l2 - 1 and s[j] < g[i]:
                j += 1
            if s[j] >= g[i]:
                cnt += 1
            if j == l2 - 1:
                break
            j += 1
        return cnt