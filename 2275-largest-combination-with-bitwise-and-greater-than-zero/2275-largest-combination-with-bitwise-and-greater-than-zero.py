class Solution:
    def largestCombination(self, nums: List[int]) -> int:
        # create a hashmap and count how often each bit is represented, return max
        mp = {}
        
        for num in nums:
            for i in range(25):
                if num & (1 << i):
                    mp[i] = mp.get(i, 0) + 1
        
        return max(mp.values())