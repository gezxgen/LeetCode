class Solution:
    def compressedString(self, word: str) -> str:
        # create stack of pairs
        stack = []
        for char in word:
            if stack and stack[-1][0] == char and stack[-1][1] != 9:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])
        
        # create string from stack
        comp = ""
        for char, count in stack:
            comp += str(count) + char
        return comp