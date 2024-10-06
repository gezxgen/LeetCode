class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        m, n = len(matrix), len(matrix[0])
        L, R = 0, m * n - 1
        
        while L <= R:
            M = (L + R) // 2
            i, j = divmod(M, n)
            if matrix[i][j] < target:
                L = M + 1
            elif matrix[i][j] > target:
                R = M - 1
            else:
                return True
        return False