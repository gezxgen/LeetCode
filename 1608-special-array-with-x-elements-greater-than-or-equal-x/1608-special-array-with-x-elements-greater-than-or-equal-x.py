class Solution:
    def specialArray(self, nums: List[int]) -> int:
        td = set()
        x, t = 0, 0
        
        while x not in td:
            td.add(x)
            
            for n in nums:
                if n >= x:
                    t += 1
                    
            if t > x:
                x += 1
            elif t < x:
                x -= 1
            else:
                return x
            t = 0
            
        return -1