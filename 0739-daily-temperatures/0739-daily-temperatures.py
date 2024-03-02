class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [1]     # variables
        stack[0] = 0
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):          # For loop O(n)
            while stack and temperatures[i] > temperatures[stack[-1]]:
                popped = stack[-1]
                result[popped] = i - stack.pop()    # Pop as long as temp > top of stack
            stack.append(i)
        return result
        