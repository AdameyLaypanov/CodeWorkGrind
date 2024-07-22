class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        pref_s = [0] * (n + 1)

        for i in range(n):
            pref_s[i + 1] = pref_s[i] + gain[i]
        return max(pref_s)