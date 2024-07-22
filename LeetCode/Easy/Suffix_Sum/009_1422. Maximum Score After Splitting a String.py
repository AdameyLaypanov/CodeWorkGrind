class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        pref_s = [0] * n
        suff_s = [0] * n

        pref_s[0] = 1 if s[0] == '0' else 0
        suff_s[-1] = 1 if s[-1] == '1' else 0

        for i in range(1, n):
            pref_s[i] = pref_s[i - 1] + (1 if s[i] == '0' else 0)

        for i in range(n - 2, -1, -1):
            suff_s[i] = suff_s[i + 1] + (1 if s[i] == '1' else 0)

        maximum = 0
        for i in range(n - 1):
            maximum = max(maximum, pref_s[i] + suff_s[i + 1])

        return maximum