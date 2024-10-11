class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L, R = 0, 0
        sm, size = 0, len(nums) + 1
        
        while R < len(nums):
            sm += nums[R]
            
            while sm >= target:
                size = min(size, R - L + 1)
                sm -= nums[L]
                L += 1
            
            R += 1
        
        return size if size <= len(nums) else 0