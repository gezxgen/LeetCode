class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        return gcd(*list(Counter(deck).values())) > 1