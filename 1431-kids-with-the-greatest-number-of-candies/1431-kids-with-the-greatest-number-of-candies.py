class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx: int = max(candies) - extraCandies
        
        for i in range(len(candies)):
            candies[i] = candies[i] >= mx
        
        return candies