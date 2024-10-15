class Solution:
    def arraySign(self, nums: List[int]) -> int:
        return 0 if 0 in nums else (-1)**(len([i for i in nums if i < 0]) % 2)