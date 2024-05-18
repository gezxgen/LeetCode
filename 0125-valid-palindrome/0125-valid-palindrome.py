class Solution:
    def isPalindrome(self, s: str) -> bool:
        translator = str.maketrans('', '', string.punctuation)  # make a translation table
        s = s.translate(translator).lower().replace(" ", "")    # remove all the punctuation and rest
        L, R = 0, len(s) - 1
    
        return s == s[::-1]
        