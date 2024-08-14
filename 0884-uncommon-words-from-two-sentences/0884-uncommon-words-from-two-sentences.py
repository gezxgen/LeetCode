class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # make a dict of all words an a counter of occurence
        # return all with a counter of 1
        w = {}
        r = []
        w1=s1.split(" ")
        w2=s2.split(" ")
        
        for wd in w1:
            if wd in w:
                w[wd] += 1
            else:
                w[wd] = 1
        
        for wd in w2:
            if wd in w:
                w[wd] += 1
            else:
                w[wd] = 1
        
        for i in w:
            if w[i] == 1:
                r.append(i)
        return r
        