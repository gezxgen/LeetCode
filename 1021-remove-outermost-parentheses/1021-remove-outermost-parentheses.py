class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack_now = []
        stack_done = []
        counter = 0

        # A outer layer is done when stack is empty
        for c in s:
            if c == "(":                # Add opening parantesy
                counter += 1
                stack_now.append("(")
            elif c == ")":
                counter -= 1
                stack_now.append(")")
                if counter == 0:
                    stack_now.pop(0)            # Clear the outer
                    stack_now.pop() 
                    stack_done += stack_now     # Add the inner
                    stack_now.clear()           # Clear the inner
        return ''.join(stack_done)