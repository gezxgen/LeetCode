class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        stack1, stack2, i = [], [], 0
        
        for string in word1:
            for char in string:
                stack1.append(char)
                
        for string in word2:
            for char in string:
                stack2.append(char)
        
        return stack1 == stack2