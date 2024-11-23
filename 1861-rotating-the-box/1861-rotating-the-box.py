class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows, columns = len(box), len(box[0])
        # adjust the array with gravity
        # go through each array
        for line in box:
            # keep left pointer at free index and right for every index
            L = float("inf")
            for R in range(columns - 1, -1, -1):
                # fill out the array
                # if place is obstacle
                if line[R] == "*":
                    L = float("inf")
                    continue
                
                # if place is empty
                if line[R] == "." and L > columns:
                    L = R
                    continue
                
                # if place is a stone
                if line[R] == "#"and L < columns:
                    line[R] = "."
                    line[L] = "#"
                    while L > R and line[L] != ".":
                        L -= 1
        
        # return in vertical format
        res = [["." for _ in range(rows)] for _ in range(columns)]
        
        for i in range(rows):
            for j in range(columns):
                res[j][i] = box[i][j]
            
        return [reversed(res[i]) for i in range(columns)]