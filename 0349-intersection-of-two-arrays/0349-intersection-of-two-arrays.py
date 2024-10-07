class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # hash nums1 and nums2
        d1, d2 = {}, {}
        for num in nums1:
            d1[num] = d1.get(num, 0) + 1
        for num in nums2:
            d2[num] = d2.get(num, 0) + 1
        
        res = []
        for key in d1:
            if key in d2:
                res.append(key)
        
        return res
        # go through nums1 and check if key in nums2
        # if so, append key to result