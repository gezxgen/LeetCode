class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # create a new 2D array res, where 0 represents free
        res = [[0 for _ in range(n)] for _ in range(m)]
            
        # fill in all guards (2's)
        for i, j in guards:
            res[i][j] = 2
            
        # fill in all walls (1's)
        for i, j in walls:
            res[i][j] = 1
            
        # for every guard
        for i, j in guards:
            # go up
            x = i - 1
            while x >= 0 and (res[x][j] == 0 or res[x][j] == 3):  # if end / wall / guard break
                res[x][j] = 3                      # else fill with 3
                x -= 1
            
            # go down
            x = i + 1
            while (x < m) and (res[x][j] == 0 or res[x][j] == 3):
                res[x][j] = 3
                x += 1
            
            # go left
            y = j - 1
            while y >= 0 and (res[i][y] == 0 or res[i][y] == 3):
                res[i][y] = 3
                y -= 1
            
            # go right
            y = j + 1
            while y < n and (res[i][y] == 0 or res[i][y] == 3):
                res[i][y] = 3
                y += 1
                
        # return number of free cells
        return sum(row.count(0) for row in res)