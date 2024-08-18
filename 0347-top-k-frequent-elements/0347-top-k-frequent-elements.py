class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = []
        c = {}
        for n in nums:
            c[n] = 1 + c.get(n, 0)
        for ky, v in c.items():
            heapq.heappush(h, (-v, ky))
        r = []
        while len(r) < k:
            r.append(heapq.heappop(h)[1])
        return r