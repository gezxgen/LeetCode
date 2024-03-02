class Solution:
    def isValid(self, s: str) -> bool:
        # Create variables
        opcl = dict(('()', '[]', '{}'))
        stack = []
        # For loop
        for idx in s:
            if idx in '([{':                                    # If opening, append
                stack.append(idx)
            elif len(stack) == 0 or idx != opcl[stack.pop()]:   # If closing and empty or wrong bracket
                return False
        return len(stack) == 0