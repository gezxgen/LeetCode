class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        a=""
        v.sort()
        f=v[0]
        l=v[-1]
        for i in range(min(len(f), len(l))):
            if(f[i] != l[i]):
                return a
            a+=f[i]
        return a 