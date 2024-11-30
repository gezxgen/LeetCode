class Solution:
    def findMedianSortedArrays(self, nums: List[int], nums2: List[int]) -> float:
        nums, n = sorted(nums + nums2), len(nums) + len(nums2)
        return nums[n // 2] if n % 2 == 1 else (nums[n // 2 - 1] + nums[ceil(n / 2)]) / 2