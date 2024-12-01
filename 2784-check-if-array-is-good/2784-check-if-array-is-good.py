class Solution:
    def isGood(self, N):
        return False if max(N) != len(N) - 1 else all([n == i + 1 for i, n in enumerate(sorted(N)[:-1])])