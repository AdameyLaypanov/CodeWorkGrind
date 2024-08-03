class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        pref_s = [0] * n

        for i in range(n):
            if hours[i] > 8:
                pref_s[i] = 1
            else:
                pref_s[i] = -1

        for i in range(1, n):
            pref_s[i] += pref_s[i - 1]

        pr_map = {}
        count = 0

        for i in range(n):
            if pref_s[i] > 0:
                count = i + 1
            else:
                if pref_s[i] - 1 in pr_map:
                    count = max(count, i - pr_map[pref_s[i] - 1])
                if pref_s[i] not in pr_map:
                    pr_map[pref_s[i]] = i

        return count
