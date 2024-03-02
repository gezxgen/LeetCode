class Solution:
    def maxDepth(self, s: str) -> int:
        length = 0
        max_len = 0

        for char in s:
            if char == "(":
                length += 1
                if length > max_len:
                    max_len = length
            elif char == ")":
                length -= 1
        
        return max_len