class Solution:
    def compressedString(self, word: str) -> str:
        # create stack of pairs
        stack, comp = [], ""
        for char in word:
            if stack and (stack[-1][0] != char or stack[-1][1] == 9):
                comp += str(stack[-1][1]) + stack[-1][0]
            if stack and stack[-1][0] == char and stack[-1][1] != 9:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])
        return comp + str(stack[-1][1]) + stack[-1][0]