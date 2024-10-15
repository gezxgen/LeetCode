class Solution:
    def arraySign(self, ns: List[int]) -> int:
        cnt = 0
        for n in ns:
            if n == 0:
                return 0
            if n < 0:
                cnt +=1
        return 1 if cnt % 2 == 0 else -1