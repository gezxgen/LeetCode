class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        cur, res = [], []
        
        def backtrack(i, nums, cur, res):
            if i == len(nums):
                res.append(cur.copy())
                return
            
            cur.append(nums[i])
            backtrack(i + 1, nums, cur, res)
            cur.pop()
            
            backtrack(i + 1, nums, cur, res)
        
        backtrack(0, nums, cur, res)
        return res