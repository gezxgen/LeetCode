class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(curSet, n):
            if len(curSet) == n:
                res.append(curSet.copy())
                return
            
            for num in nums:
                if num in curSet:
                    continue
                    
                curSet.append(num)
                backtrack(curSet, n)
                curSet.pop()
        
        backtrack([], len(nums))
        return res