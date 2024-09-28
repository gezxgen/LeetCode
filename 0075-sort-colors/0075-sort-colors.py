class Solution:
    def sortColors(self, nums: List[int]) -> None:
        cnt0: int = 0
        cnt1: int = 0
        
        # count nums of 0, nums of 1
        for num in nums:
            if num == 0:
                cnt0 += 1
            elif num == 1:
                cnt1 += 1
        
        # replace elemets
        for i in range(cnt0):
            nums[i] = 0
        for i in range(cnt0, cnt1+cnt0):
            nums[i] = 1
        for i in range(cnt0+cnt1, len(nums)):
            nums[i] = 2