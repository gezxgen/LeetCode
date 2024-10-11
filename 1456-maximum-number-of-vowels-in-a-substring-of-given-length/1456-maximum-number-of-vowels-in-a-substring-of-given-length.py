class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        s = s.lower()
        cnt = sum([1 for i in range(k) if s[i] in vowels])
        mx = cnt
        
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                cnt -= 1
            if s[i] in vowels:
                cnt += 1
            mx = max(mx, cnt)
        return mx