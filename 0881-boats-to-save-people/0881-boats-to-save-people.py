class Solution:
    def numRescueBoats(self, nums: List[int], target: int) -> int:
        nums.sort()
        boats, L, R, = 0, 0, len(nums)-1
        
        while L <= R:
            if nums[L] + nums[R] <= target:
                L += 1
            R -= 1
            boats += 1
        
        return boats
        