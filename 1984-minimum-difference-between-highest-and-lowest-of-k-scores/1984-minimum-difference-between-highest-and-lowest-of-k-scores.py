class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        cur, mn = 0, 100000
        L, R, n = 0, k - 1, len(nums)
        
        while R < n:
            mn = min(mn, nums[R] - nums[L])
            L, R = L + 1, R + 1
        return mn
        