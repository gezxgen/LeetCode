class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)                          # create variables
        counter = 1
        
        while counter <= n and word2 != "":     # go through as long as not at the end
            word1 = word1[:counter] + word2[0] + word1[counter:]
            
            word2 = word2[1:]                   # update
            counter += 2
            n = len(word1)
        
        word1 = word1 + word2                   # append rest
        
        return word1
             