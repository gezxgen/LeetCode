class Solution:
    def maxArea(self, nums: List[int]) -> int:
        tot, L, R = 0, 0, len(nums)-1
        
        while L < R:
            tot = max(tot, (R-L)*min(nums[L], nums[R]))
            if nums[L] < nums[R]:
                L += 1
            else:
                R -= 1
        return tot