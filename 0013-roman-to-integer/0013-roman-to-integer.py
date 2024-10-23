class Solution:
    def romanToInt(self, s: str) -> int:
        total, lut = 0, {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for i in range(len(s) - 1):
            if lut[s[i]] < lut[s[i + 1]]:
                total -= lut[s[i]]
            else:
                total += lut[s[i]]
        total += lut[s[-1]]
        return total