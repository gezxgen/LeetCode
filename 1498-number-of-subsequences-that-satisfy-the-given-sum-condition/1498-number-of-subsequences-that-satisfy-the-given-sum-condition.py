class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        cnt, mod, R = 0, 10**9 + 7, len(nums) - 1
        for L in range(len(nums)):
            while nums[L] + nums[R] > target and L <= R:
                R -= 1
            if L <= R:
                cnt += 2**(R - L)
                cnt %= mod
        return cnt