class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        cnt: int = 0
        
        for i in range(len(nums)):
            if nums[i] < k:
                cnt += 1
        
        return cnt