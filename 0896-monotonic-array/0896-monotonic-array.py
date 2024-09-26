class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        val: bool = True
        
        # check if increasing
        for i in range(len(nums)-1):
            if not (nums[i] <= nums[i+1]):
                val = False
                break
        
        # return if increasing
        if val:
            return True
        val = True
        
        # cheack if decreasing
        for i in range(len(nums)-1):
            if not (nums[i] >= nums[i+1]):
                val = False
                break
        
        # return result
        return val