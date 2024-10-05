class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # binary search your way to element
        L, R = 0, len(nums)-1
        while L <= R:
            M = (L + R) // 2
            if nums[M] < target:
                L = M + 1
            elif nums[M] > target:
                R = M - 1
            else:
                break
                
        # return if not found
        if (not nums) or (nums[M] != target):
            return [-1, -1]
        
        # else search for leftest value
        for L in range(M, -1, -1):
            if nums[L] != target:
                break
        if nums[L] != target:
            L += 1
        
        # search for rightest value
        for R in range(M, len(nums)):
            if nums[R] != target:
                break
        if nums[R] != target:
            R -= 1
        
        return [L, R]