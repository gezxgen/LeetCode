class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        a = []
        for i in range(len(nums) // 2):
            a.append((nums[i] + nums.pop()) / 2)
        return min(a)
        