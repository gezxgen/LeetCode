class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        b = len(candyType) // 2
        a = len(set(candyType))
        return min(a, b)