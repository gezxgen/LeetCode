class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        L, R = 0, len(nums) - 1
        while L <= R:
            while L <= R and nums[L] % 2 == 1:
                nums[L], nums[R] = nums[R], nums[L]
                R -= 1
            L += 1
        return nums