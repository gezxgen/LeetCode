class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        if n == 0:                      # if arry is empty
            return []
        if k == 0:                      # if k is zero
            return nums
        while k > n:                    # if k ist bigger than array
            k -= n
        for i in range(k):              # rotate the array
            nums.insert(0, nums.pop())
        