class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n1, n2, i, j = len(str1), len(str2), 0, 0
        while i < n1 and j < n2:
            i, j = i + 1, j + 1 if (ord(str2[j]) - ord(str1[i]) + 26) % 26 <= 1 else j
        return j == n2