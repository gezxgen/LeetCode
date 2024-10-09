class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        L, R, res = 0, n - 1, []
        while len(res) != len(nums):
            res.append(nums[L])
            L += 1
            if L <= R:
                res.append(nums[R])
                R -= 1
        return res