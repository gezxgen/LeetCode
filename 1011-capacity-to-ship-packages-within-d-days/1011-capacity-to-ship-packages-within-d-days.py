class Solution:
    def shipWithinDays(self, weights: List[int], day: int) -> int:
        l = max(weights)
        r = sum(weights)

        def days(cap: int) -> int:
            day = 1
            cp = 0
            for w in weights:
                if cp + w > cap:
                    day += 1
                    cp = w
                else:
                    cp += w
            return day

        while l < r:
            m = (l + r) // 2
            if days(m) <= day:
                r = m
            else:
                l = m + 1

        return l