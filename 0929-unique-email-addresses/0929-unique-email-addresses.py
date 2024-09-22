class Solution:
    def numUniqueEmails(self, s: List[str]) -> int:
        u = set()
    
        for e in s:
            l, d = e.split('@')
            l = l.split('+')[0]
            l = l.replace('.', '')
            m = l + '@' + d
            u.add(m)

        return len(u)