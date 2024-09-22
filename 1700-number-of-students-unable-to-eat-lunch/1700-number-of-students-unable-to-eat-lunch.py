class Solution:
    def countStudents(self, s: List[int], w: List[int]) -> int:
        c = 0
        
        while c < 2*len(s):
            if w[0] == s[0]:
                w.pop(0)
                s.pop(0)
                c = 0
            else:
                s.append(s.pop(0))
            
            c += 1
        return len(w)