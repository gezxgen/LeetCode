class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mp, n, res = {}, len(nums) / 3, []
        for num in nums:
            mp[num] = mp.get(num, 0) + 1
        
        for key, val in mp.items():
            if val > n:
                res.append(key)
        
        return res