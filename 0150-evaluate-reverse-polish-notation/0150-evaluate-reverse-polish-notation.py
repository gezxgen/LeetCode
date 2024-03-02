class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []      # Create Variables
        first = 0
        last = 0

        for token in tokens:                                # go through every digit
            match token:                                    # match to find the operand
                case "+":
                    first, last = stack.pop(), stack.pop()  # save popped elements
                    stack.append(first + last)              # operate the last two added nums
                case "-":
                    first, last = stack.pop(), stack.pop()
                    stack.append(int(last - first))
                case "*":
                    first, last = stack.pop(), stack.pop()
                    stack.append(first * last)
                case "/":
                    first, last = stack.pop(), stack.pop()
                    stack.append(int(last / first))
                case _:
                    stack.append(int(token))                # add number to stack

        return stack[0]