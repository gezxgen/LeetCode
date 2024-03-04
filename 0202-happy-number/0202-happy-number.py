class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        
        while n != 1:
            if n in nums:
                return False
            nums.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
            
        return True