class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        current_diff = 2147483647
        all_time_diff = 2147483647
        nums.sort()
        l = 0
        r = k - 1
        
        while r < len(nums):
            current_diff = nums[r] - nums[l]
            if current_diff < all_time_diff:
                all_time_diff = current_diff
            l += 1
            r += 1
        
        return all_time_diff
        
        