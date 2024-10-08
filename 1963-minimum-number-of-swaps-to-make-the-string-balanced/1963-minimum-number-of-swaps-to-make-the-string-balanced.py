class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        
        for char in s:
            if (char == "]") and stack and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(char)
        return int(ceil((len(stack) // 2) / 2))
            