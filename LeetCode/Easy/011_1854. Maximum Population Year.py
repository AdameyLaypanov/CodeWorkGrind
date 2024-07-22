class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        used = [0] * 2051
        for i in range(len(logs)):
            birth, death = logs[i]
            used[birth] += 1
            used[death] -= 1

        max_man = 0
        curr = 0
        early_year = 0

        for i in range(1950, 2051):
            curr += used[i]
            if curr > max_man:
                max_man = curr
                early_year = i
        return early_year