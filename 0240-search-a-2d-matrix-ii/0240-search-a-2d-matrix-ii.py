class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if (not matrix) or (not len(matrix)) or (not len(matrix[0])):
            return False
        
        row, col = 0, len(matrix[0])-1
        
        while (col >= 0 and row <= len(matrix)-1):
            if (target < matrix[row][col]):
                col -= 1
            elif (target > matrix[row][col]):
                row += 1
            else:
                return True
        
        return False