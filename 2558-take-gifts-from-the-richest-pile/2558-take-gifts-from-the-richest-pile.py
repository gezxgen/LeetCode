class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts.sort()
        
        for _ in range(k):
            insort(gifts, int(sqrt(gifts.pop())))
            
        return sum(gifts)        