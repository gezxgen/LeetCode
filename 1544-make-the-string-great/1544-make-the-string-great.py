class Solution:
    def makeGood(self, s: str) -> str:
        stack = ""
        for char in s:
            if stack and (ord(stack[-1]) - 32 == ord(char) or ord(stack[-1]) == ord(char) - 32):
                stack = stack[:-1]
            else:
                stack += char
        return stack