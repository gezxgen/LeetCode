class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        L, R = 0, 0
        is_break: bool = False
        
        for strn in words:
            is_break = False
            L, R = 0, len(strn)-1
            
            while L < R:
                if strn[L] != strn[R]:
                    is_break = True
                    break
                L += 1
                R -= 1
            
            if not is_break:
                return strn
        
        return ""