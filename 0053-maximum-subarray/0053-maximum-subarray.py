class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]    # Set default values
        curSum = 0

        for n in nums:      # Go through the array and update sums
            curSum = max(curSum, 0)
            curSum += n
            maxSum = max(curSum, maxSum)
        return maxSum
