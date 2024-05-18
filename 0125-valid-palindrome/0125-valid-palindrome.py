class Solution:
    def isPalindrome(self, s: str) -> bool:
        translator = str.maketrans('', '', string.punctuation)  # make a translation table
        s = s.translate(translator).lower().replace(" ", "")    # remove all the punctuation and rest
        L, R = 0, len(s) - 1
        
        while L < R:
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1
        return True