class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L, R, n = 0, 0, len(nums)
        sm, size = 0, n + 1
        
        while R < n:
            sm += nums[R]
            while sm >= target:
                size = min(size, R - L + 1)
                sm -= nums[L]
                L += 1
            R += 1
        return size if size <= n else 0