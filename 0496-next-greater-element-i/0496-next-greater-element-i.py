class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n: int = len(nums1)
        m: int = len(nums2)
        dex: int = 0
        res: list[int] = [-1 for _ in range(len(nums1))]
        
        for i in range(n):
            for j in range(m):
                if nums2[j] == nums1[i]:
                    dex = j
            
            for j in range(dex, m):
                if nums2[j] > nums2[dex]:
                    res[i] = nums2[j]
                    break
        
        return res