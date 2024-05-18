class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1
        memory = ""
        
        while left < right:
            memory = s[left]
            s[left] = s[right] 
            s[right] = memory
            
            left += 1
            right -= 1
        

        