class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for num in nums2:
            nums1.insert(0, num)
            nums1.pop()
        nums1.sort()
        