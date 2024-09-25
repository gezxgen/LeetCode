class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        j: int = 0
        n: int = len(nums) - 1
        count: int = 0
            
        nums.sort()
        
        for i in range(n):
            j = i + 1
            while (j <= n) and (nums[i] == nums[j]):
                count += 1
                j += 1
        
        return count