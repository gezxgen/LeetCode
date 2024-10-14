class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack: list[list[str, int]] = []
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                if stack and stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])
                    
        return "".join(c * k for c, k in stack)