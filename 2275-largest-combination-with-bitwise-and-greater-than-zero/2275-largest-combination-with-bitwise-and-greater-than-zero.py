class Solution:
    def largestCombination(self, nums: List[int]) -> int:
        # create a hashmap and count how often each bit is represented, return max
        ls = [0 for _ in range(24)]
        
        for num in nums:
            for i in range(24):
                if num & (1 << i):
                    ls[i] += 1
        
        return max(ls)