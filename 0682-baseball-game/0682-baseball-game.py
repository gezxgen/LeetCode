class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for opp in operations:
            if opp == "+":
                stack.append(stack[-1] + stack[-2])
            elif opp == "D":
                stack.append(stack[-1]*2)
            elif opp == "C":
                stack.pop()
            else:
                stack.append(int(opp))
        return sum(stack)