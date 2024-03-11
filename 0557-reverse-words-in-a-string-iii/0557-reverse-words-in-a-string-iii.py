class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)     # convert to list
        L, R = 0, 0     # make two pointers
        l, r = 0, 0     # make copies to swap
        placeholder = 0
        current = ""
        n = len(s)
        
        while n != R:   # repeat until you're done, or you hit the length of the array         
            if s[R] == " " or R == n - 1:   # take the right pointer until he hits a space
                if R == n - 1:
                    placeholder = L
                l, r = L, R                 # set the copies
                while l < r:                # reverse all elements until the space
                    current = s[l]          # swap positions
                    s[l] = s[r - 1]
                    s[r - 1] = current
                    r -= 1                  # update the copies
                    l += 1
                L = R + 1                   # move left pointer to new word
            R += 1
        
        s.insert(placeholder, s[n - 1])     # swap the last element
        s.pop()
        
        return "".join(s)                   # convert back to string
        