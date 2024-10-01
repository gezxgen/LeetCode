class Solution:
    def maxArea(self, nums: List[int]) -> int:
        tot, cur, L, R = 0, 0, 0, len(nums)-1
        
        while L < R:
            cur = min(nums[L], nums[R]) * (R-L)
            tot = max(tot, cur)
            if nums[L] < nums[R]:
                L += 1
            else:
                R -= 1
        return tot