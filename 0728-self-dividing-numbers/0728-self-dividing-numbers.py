class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def check(num):
            for digit in str(num):
                n = int(digit)
                if not n or num % n != 0:
                    return False 
            return True
        
        res = []
        for i in range(left, right + 1):
            if check(i):
                res.append(i)
        return res