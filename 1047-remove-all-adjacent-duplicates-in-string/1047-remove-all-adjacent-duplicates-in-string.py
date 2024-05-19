class Solution:
    def removeDuplicates(self, s: str) -> str:
        k = []
        
        for c in s:
            if k and k[-1] == c:
                k.pop()
            else:
                k.append(c)
        
        return "".join(k)
    