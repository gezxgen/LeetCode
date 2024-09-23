class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c: int = 0
        t: int = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                t = nums[c]
                nums[c] = nums[i]
                nums[i] = t
                c += 1
                
        return c