class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merge
        for num in nums2:
            nums1.append(num)
        nums1.sort()

        # Delete unnecessary elements
        while len(nums1) > 2:
            nums1.pop(0)
            nums1.pop()

        # Return median
        if len(nums1) == 1:
            return nums1[0] + 0.0
        else:
            return (nums1[0] + nums1[1]) / 2.0