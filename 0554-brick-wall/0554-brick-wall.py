class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        freq, mx = {}, 0
        for row in range(len(wall)):
            edge = 0
            for brick in range(len(wall[row])-1):
                edge += wall[row][brick]
                freq[edge] = freq.get(edge, 0) + 1
                mx = max(mx, freq[edge])
        return len(wall) - mx
            
        