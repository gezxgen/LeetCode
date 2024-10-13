class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        L1, L2, n1, n2 = 0, 0, len(nums1), len(nums2)
        res: list[list[int]] = []
        
        while L1 < n1 and L2 < n2:
            if nums1[L1][0] < nums2[L2][0]:
                res.append(nums1[L1])
                L1 += 1
            elif nums1[L1][0] > nums2[L2][0]:
                res.append(nums2[L2])
                L2 += 1
            else:
                res.append([nums1[L1][0], nums1[L1][1] + nums2[L2][1]])
                L1 += 1
                L2 += 1
        
        if L1 == n1 and L2 == n1:
            return res
        elif L1 == n1:
            while L2 != n2:
                res.append(nums2[L2])
                L2 += 1
        else:
            while L1 != n1:
                res.append(nums1[L1])
                L1 += 1
            
        return res