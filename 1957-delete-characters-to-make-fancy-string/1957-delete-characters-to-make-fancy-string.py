class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) <= 2:
            return s
        
        stack = [s[0], s[1]]
        
        for char in s[2:]:
            if stack[-1] != char or stack[-2] != char:
                stack.append(char)
            
        return "".join(stack)