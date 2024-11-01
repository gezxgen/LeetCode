class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = float("inf")
        n = len(nums) - 1
        
        nums.sort()
        for i in range(n - 1):
            L, R = i + 1, n
            while L < R:
                sm = nums[i] + nums[L] + nums[R]
                
                if abs(target - sm) < abs(target - closest):
                        closest = sm
                        
                if sm < target:
                    L += 1
                elif sm > target:
                    R -= 1
                else:
                    return target
        
        return closest