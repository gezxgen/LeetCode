class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nf = {}
        o = []

        if k == len(nums):
            return nums
        
        for n in nums:
            if n in nf.keys():
                nf[n] += 1
            else:
                nf[n] = 1
            
        sd = dict(sorted(nf.items(), key=lambda x: x[1], reverse=True))

        for i in range(k):
            ky, v = list(sd.items())[i]
            o.append(ky)
        
        return o
