class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = [0 for _ in range(len(nums))]
        ret = []
        
        for num in nums:
            res[num - 1] = 1
        
        for i in range(len(res)):
            if not res[i]:
                ret.append(i + 1)
        
        return ret