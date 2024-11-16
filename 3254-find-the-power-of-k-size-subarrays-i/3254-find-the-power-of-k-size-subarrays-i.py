class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans, score = [-1] * (n - k + 1), 0
        
        for i in range(n):
            score = score + 1 if i and nums[i - 1] + 1 == nums[i] else 0
            if score >= k - 1:
                ans[i - k + 1] = nums[i]
        
        return ans;