class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # make a dict of all words an a counter of occurence
        # return all with a counter of 1
        words = {}
        res = []
        
        for word in s1.split(" "):
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
        
        for word in s2.split(" "):
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
        
        for item in words:
            if words[item] == 1:
                res.append(item)
        return res
        