class Solution:
    def arraySign(self, nums: List[int]) -> int:
        def signFunc(x):
            if x < 0:
                return -1
            elif x > 0:
                return 1
            return 0
        
        pw = 1
        for num in nums:
            pw *= num
        
        return signFunc(pw)