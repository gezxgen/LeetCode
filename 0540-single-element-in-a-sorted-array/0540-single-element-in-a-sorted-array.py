class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n: int = len(nums) - 1
        L, R = 0, n
        
        while L <= R:
            M = (L + R) // 2
            
            if M > 0 and nums[M] == nums[M - 1]:
                if (M + 1) % 2 == 0:
                    L = M + 1
                else:
                    R = M - 2
            elif M < n and nums[M] == nums[M + 1]:
                if M % 2 == 0:
                    L = M + 2
                else:
                    R = M - 1
            else:
                return nums[M]