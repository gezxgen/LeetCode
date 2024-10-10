class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res, mp = [0, 0], {i: 0 for i in range(len(nums)+1)}
        
        for num in nums:
            mp[num] += 1
        
        for i in range(len(mp)):
            if mp[i] == 0:
                res[1] = i
            elif mp[i] == 2:
                res[0] = i
        
        return res