class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, cur = [], []
        
        def backtracking(nums: List[int], l: int, n: int, i: int, totComb: List[int], curComb: List[int]) -> None:
            sm = sum(curComb)   # calculate sum of current combination
            
            # append if target is found
            if sm == n:
                totComb.append(curComb.copy())
                return
            
            # return if sum is too big
            if sm > n or i == l:
                return
            
            # if it is smaller, include and not include the value
            curComb.append(nums[i])
            backtracking(nums, l, n, i, totComb, curComb)
            curComb.pop()
            
            backtracking(nums, l, n, i + 1, totComb, curComb)
            

        backtracking(candidates, len(candidates), target, 0, res, cur)
        return res