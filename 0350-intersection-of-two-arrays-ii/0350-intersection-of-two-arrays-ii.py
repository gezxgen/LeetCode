class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map1 = {}               # Create the variables
        map2 = {}
        map_res = {}
        res = []

        for num in nums1:       # Create a HashMap of nums1 as well as nums2
            if num in map1:
                map1[num] += 1
            else:
                map1[num] = 1
        
        for num in nums2:
            if num in map2:
                map2[num] += 1
            else:
                map2[num] = 1
        
        for key in map1:        # Create a third HashMap with only intersected nums
            if key in map2.keys():
                if map1[key] > map2[key]:   # The value of the nums is wich ever is smaller
                    map_res[key] = map2[key]
                else:
                    map_res[key] = map1[key]
        
        # Put the number as often in the solution as given
        for key in map_res:
            for i in range(map_res[key]):
                res.append(key)
        
        return res