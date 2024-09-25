class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ctn: int = 0
        tot: int = sum(nums)
        
        for i in range(len(nums)):
            if ctn == (tot - ctn - nums[i]):
                return i
            ctn += nums[i]
        
        return -1