class Solution:
    def sortColors(self, nums: List[int]) -> None:
        p0, mid, p2 = 0, 0 , len(nums) - 1
        
        while mid <= p2:
            if nums[mid] == 0:
                nums[p0], nums[mid] = nums[mid], nums[p0]
                p0 += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[p2], nums[mid] = nums[mid], nums[p2]
                p2 -= 1
            