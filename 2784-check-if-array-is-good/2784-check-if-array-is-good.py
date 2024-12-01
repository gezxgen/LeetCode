class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        
        if nums[-1] != len(nums) - 1:
            return False
        
        for i, num in enumerate(nums[:-1]):
            if num != i + 1:
                return False
        
        return True
        