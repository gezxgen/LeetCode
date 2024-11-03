class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        n = len(s)
        for i in range(n):
            if s[i + 1:n] + s[:i + 1] == goal:
                return True
        
        return False