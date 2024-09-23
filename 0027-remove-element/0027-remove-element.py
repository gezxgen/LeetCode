class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        temp = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                temp = nums[counter]
                nums[counter] = nums[i]
                nums[i] = temp
                counter += 1
                
        return counter