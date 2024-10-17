class Solution:
    def interchangeableRectangles(self, rec: List[List[int]]) -> int:
        mp = {}
        cnt = 0
        
        for width, height in rec:
            ratio = width / height
            if ratio in mp:
                mp[ratio] += 1
                cnt += mp[ratio]
            else:
                mp[ratio] = 0
        
        return cnt