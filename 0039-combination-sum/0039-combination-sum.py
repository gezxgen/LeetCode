class Solution:
    def combinationSum(self, candidates, target):
        res, cur = [], []
        
        def backtracking(nums, l, n, i, totComb, curComb, sm):
            # append if target is found
            if sm == n:
                totComb.append(curComb.copy())
                return
            
            # return if sum is too big
            if sm > n or i == l:
                return
            
            # if it is smaller, include and not include the value
            curComb.append(nums[i])
            backtracking(nums, l, n, i, totComb, curComb, sm + nums[i])
            curComb.pop()
            
            backtracking(nums, l, n, i + 1, totComb, curComb, sm)
            

        backtracking(candidates, len(candidates), target, 0, res, cur, 0)
        return res