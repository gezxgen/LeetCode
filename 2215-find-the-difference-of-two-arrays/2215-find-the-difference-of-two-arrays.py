class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res, mp1, mp2 = [[] for _ in range(2)], {}, {}
        
        for num in nums1:
            mp1[num] = mp1.get(num, 0) + 1
        for num in nums2:
            mp2[num] = mp2.get(num, 0) + 1
        
        for num in nums1:
            if not mp2.get(num, 0) and num not in res[0]:
                res[0].append(num)
        for num in nums2:
            if not mp1.get(num, 0) and num not in res[1]:
                res[1].append(num)
        
        return res